IDEAL_SECTIONS = ["summary", "skills", "experience", "education", "projects", "contact"]


def check_resume_structure(resume_text):
    """
    Checks whether common resume sections are present in the resume text
    and returns a checklist comparing it against an ideal resume structure
    """
    text_lower = resume_text.lower()
    section_status = {}

    for section in IDEAL_SECTIONS:
        section_status[section] = section in text_lower

    present_count = sum(section_status.values())
    structure_score = round((present_count / len(IDEAL_SECTIONS)) * 100, 2)

    return {
        "section_status": section_status,
        "structure_score": structure_score
    }