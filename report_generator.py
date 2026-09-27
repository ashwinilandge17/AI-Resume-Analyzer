from fpdf import FPDF

def generate_pdf_report(filename, overall_match, skill_match, academic_score,
                         matched_skills, missing_skills, ats_result, contact_info, experience_years):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Resume Analysis Report", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, f"File: {filename}", ln=True)
    pdf.cell(0, 8, f"Email: {contact_info['email']}", ln=True)
    pdf.cell(0, 8, f"Phone: {contact_info['phone']}", ln=True)
    pdf.cell(0, 8, f"Experience Detected: {experience_years} years", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Scores", ln=True)
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, f"Overall Text Match: {overall_match}%", ln=True)
    pdf.cell(0, 8, f"Skill Match: {skill_match}%", ln=True)
    pdf.cell(0, 8, f"Academic Score: {academic_score}%", ln=True)
    pdf.cell(0, 8, f"ATS Friendliness Score: {ats_result['ats_score']}%", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Matched Skills", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, ", ".join(matched_skills) if matched_skills else "None")
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Missing Skills", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, ", ".join(missing_skills) if missing_skills else "None")
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "ATS Issues", ln=True)
    pdf.set_font("Helvetica", "", 11)
    for issue in ats_result["issues"]:
        pdf.multi_cell(0, 6, f"- {issue}")

    return bytes(pdf.output())