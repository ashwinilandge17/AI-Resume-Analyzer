import spacy
from skills_list import SKILLS_DB

nlp = spacy.load("en_core_web_sm")


def extract_skills(resume_text):
    """
    Matches the resume text against the predefined skills list
    and returns all the skills found
    """
    resume_text_lower = resume_text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill.lower() in resume_text_lower:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, jd_skills):
    """
    Compares resume skills with JD skills
    and returns matched and missing skills
    """
    resume_skills_set = set(resume_skills)
    jd_skills_set = set(jd_skills)

    matched_skills = resume_skills_set.intersection(jd_skills_set)
    missing_skills = jd_skills_set - resume_skills_set

    if len(jd_skills_set) > 0:
        skill_match_percentage = round((len(matched_skills) / len(jd_skills_set)) * 100, 2)
    else:
        skill_match_percentage = 0

    return {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "skill_match_percentage": skill_match_percentage
    }


def extract_dynamic_keywords(text):
    """
    Uses spaCy to extract important noun phrases (potential skills/keywords)
    from text — without relying on any predefined list
    """
    doc = nlp(text.lower())
    keywords = set()

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip()
        if len(phrase) > 2 and not chunk.root.is_stop:
            keywords.add(phrase)

    return keywords


def compare_dynamic_skills(resume_text, jd_text):
    """
    Extracts dynamic keywords from the JD and compares them
    against the resume text (not dependent on the predefined SKILLS_DB list)
    """
    jd_keywords = extract_dynamic_keywords(jd_text)
    resume_text_lower = resume_text.lower()

    matched = set()
    missing = set()

    for keyword in jd_keywords:
        if keyword in resume_text_lower:
            matched.add(keyword)
        else:
            missing.add(keyword)

    if len(jd_keywords) > 0:
        match_percentage = round((len(matched) / len(jd_keywords)) * 100, 2)
    else:
        match_percentage = 0

    return {
        "matched_keywords": list(matched),
        "missing_keywords": list(missing),
        "dynamic_match_percentage": match_percentage
    }


# Testing
if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf

    resume_text = extract_text_from_pdf("Ashwini.pdf")
    skills_found = extract_skills(resume_text)

    print("Found Skills:")
    for skill in skills_found:
        print(f"- {skill}")

from role_skills_mapping import detect_role_and_get_skills


def compare_skills_with_role_detection(resume_skills, jd_skills, jd_text):
    """
    First compares against explicit JD skills.
    If no specific skill is found in the JD, detects the job role
    from the JD text and uses that role's typical skill set instead.
    """
    if len(jd_skills) > 0:
        final_jd_skills = jd_skills
        detected_role = None
    else:
        detected_role, role_skills = detect_role_and_get_skills(jd_text)
        final_jd_skills = role_skills

    result = compare_skills(resume_skills, final_jd_skills)
    result["detected_role"] = detected_role

    return result