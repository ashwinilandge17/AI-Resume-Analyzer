from skills_list import SKILLS_DB

def extract_skills(resume_text):
    """
    Matches the resume text against the predefined skills list
    and returns all the skills found
    """
    resume_text_lower = resume_text.lower()  # convert everything to lowercase
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


# Testing
if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf
    
    resume_text = extract_text_from_pdf("Ashwini.pdf")
    skills_found = extract_skills(resume_text)
    
    print("Found Skills:")
    for skill in skills_found:
        print(f"- {skill}")