import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills, compare_skills, compare_skills_with_role_detection
from jd_matcher import calculate_match_score
from education_matcher import extract_education_score, extract_detailed_education
from contact_extractor import extract_contact_info
from experience_extractor import extract_experience
from ats_checker import check_ats_friendliness
from suggestions import generate_suggestions
from history_manager import save_to_history, load_history
from report_generator import generate_pdf_report
from resume_structure_checker import check_resume_structure
from grammar_checker import check_spelling

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload one or more resumes and check their match with a job description!")

uploaded_files = st.file_uploader(
    "Upload Resume(s) (PDF)", type="pdf", accept_multiple_files=True
)
jd_text = st.text_area("Paste Job Description Here", height=200)

st.subheader("🎓 Education Filter")
st.caption("Leave as 'No Filter' if you don't want to apply any education criteria.")

col_a, col_b, col_c = st.columns(3)
with col_a:
    education_level = st.selectbox(
        "Education Level to Check",
        ["Overall Average", "10th", "12th", "Degree"]
    )
with col_b:
    education_filter_type = st.selectbox(
        "Filter Type",
        ["No Filter", "Minimum Required", "Maximum Allowed"]
    )
with col_c:
    education_threshold = st.number_input(
        "Threshold (%)", min_value=0, max_value=100, value=60
    )

if st.button("Analyze Resume(s)"):
    if uploaded_files and jd_text.strip() != "":

        results_summary = []

        for uploaded_file in uploaded_files:

            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            resume_text = extract_text_from_pdf(temp_path)

            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)

            overall_match = calculate_match_score(resume_text, jd_text)
            skill_comparison = compare_skills_with_role_detection(resume_skills, jd_skills, jd_text)
            edu_result = extract_education_score(resume_text)
            detailed_edu = extract_detailed_education(resume_text)
            contact_info = extract_contact_info(resume_text)
            experience_years = extract_experience(resume_text)
            ats_result = check_ats_friendliness(temp_path)
            suggestions = generate_suggestions(skill_comparison["missing_skills"])
            structure_result = check_resume_structure(resume_text)
            misspelled_words = check_spelling(resume_text)

            final_score = round(
                (overall_match + skill_comparison["skill_match_percentage"] + edu_result["average_academic_score"]) / 3,
                2
            )

            results_summary.append({
                "Resume": uploaded_file.name,
                "Final Score": final_score,
                "Skill Match %": skill_comparison["skill_match_percentage"],
                "Academic %": edu_result["average_academic_score"],
                "ATS Score": ats_result["ats_score"],
                "Structure Score": structure_result["structure_score"]
            })

            save_to_history(
                uploaded_file.name, overall_match,
                skill_comparison["skill_match_percentage"],
                edu_result["average_academic_score"]
            )

            with st.expander(f"📄 {uploaded_file.name} — Detailed Analysis", expanded=(len(uploaded_files) == 1)):

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Overall Match", f"{overall_match}%")
                with col2:
                    st.metric("Skill Match", f"{skill_comparison['skill_match_percentage']}%")
                with col3:
                    st.metric("Academic Score", f"{edu_result['average_academic_score']}%")
                with col4:
                    st.metric("ATS Score", f"{ats_result['ats_score']}%")

                st.subheader("📞 Contact Info")
                st.write(f"**Email:** {contact_info['email']}")
                st.write(f"**Phone:** {contact_info['phone']}")
                st.write(f"**Experience Detected:** {experience_years} years")

                st.subheader("🎓 Education Details")
                st.write(f"**10th:** {detailed_edu['tenth']['score']}% — {detailed_edu['tenth']['remark']}")
                st.write(f"**12th:** {detailed_edu['twelfth']['score']}% — {detailed_edu['twelfth']['remark']}")
                st.write(f"**Degree:** {detailed_edu['degree']['score']}% (equivalent) — {detailed_edu['degree']['remark']}")
                st.write(f"**Overall Average:** {edu_result['average_academic_score']}% — {edu_result['education_remark']}")

                level_map = {
                    "10th": detailed_edu["tenth"]["score"],
                    "12th": detailed_edu["twelfth"]["score"],
                    "Degree": detailed_edu["degree"]["score"],
                    "Overall Average": edu_result["average_academic_score"]
                }
                selected_score = level_map.get(education_level)

                if education_filter_type != "No Filter":
                    if selected_score is None:
                        st.warning(f"⚠️ {education_level} score not found in resume — cannot apply filter.")
                    else:
                        if education_filter_type == "Minimum Required":
                            eligible = selected_score >= education_threshold
                        else:
                            eligible = selected_score <= education_threshold

                        if eligible:
                            st.success(f"✅ Meets criteria on {education_level} ({education_filter_type}: {education_threshold}%)")
                        else:
                            st.error(f"❌ Does not meet criteria on {education_level} ({education_filter_type}: {education_threshold}%)")

                st.subheader("📈 Skill Match Chart")
                counts = [len(skill_comparison["matched_skills"]), len(skill_comparison["missing_skills"])]
                if sum(counts) > 0:
                    fig, ax = plt.subplots()
                    ax.pie(counts, labels=["Matched", "Missing"], autopct='%1.1f%%', colors=["#4CAF50", "#F44336"])
                    ax.axis("equal")
                    st.pyplot(fig)
                else:
                    st.info("No specific skills were detected in the job description to compare.")

                if skill_comparison.get("detected_role"):
                    st.info(f"Detected Job Role: {skill_comparison['detected_role'].title()} — showing typically required skills for this role")

                st.subheader("✅ Matched Skills")
                st.success(", ".join(skill_comparison["matched_skills"]) or "None")

                st.subheader("❌ Missing Skills")
                st.error(", ".join(skill_comparison["missing_skills"]) or "None")

                st.subheader("📋 Resume Structure Check (Compared to Ideal Format)")
                st.write(f"**Structure Score:** {structure_result['structure_score']}%")
                for section, present in structure_result['section_status'].items():
                    icon = "✅" if present else "❌"
                    st.write(f"{icon} {section.title()} section {'found' if present else 'not found'}")

                st.subheader("✍️ Spelling Check")
                if misspelled_words:
                    st.warning("Potentially misspelled words: " + ", ".join(misspelled_words))
                    st.caption("Note: Names, places, and company names are often flagged as 'unknown' even when spelled correctly — this is a normal limitation of dictionary-based spell checkers.")
                else:
                    st.success("No spelling issues detected!")

                st.subheader("💡 Improvement Suggestions")
                for s in suggestions:
                    st.write(f"- {s}")

                st.subheader("🔍 ATS Friendliness Check")
                for issue in ats_result["issues"]:
                    st.write(f"- {issue}")

                pdf_bytes = generate_pdf_report(
                    uploaded_file.name, overall_match,
                    skill_comparison["skill_match_percentage"],
                    edu_result["average_academic_score"],
                    skill_comparison["matched_skills"],
                    skill_comparison["missing_skills"],
                    ats_result, contact_info, experience_years
                )
                st.download_button(
                    "📥 Download PDF Report",
                    data=pdf_bytes,
                    file_name=f"{uploaded_file.name}_report.pdf",
                    mime="application/pdf"
                )

        if len(uploaded_files) > 1:
            st.subheader("🏆 Resume Ranking")
            df = pd.DataFrame(results_summary).sort_values("Final Score", ascending=False)
            st.dataframe(df, width='stretch')

    else:
        st.warning("Please upload at least one resume and enter a job description!")

st.divider()
st.subheader("🕒 Analysis History")
history = load_history()
if history:
    st.dataframe(pd.DataFrame(history), width='stretch')
else:
    st.write("No history yet.")