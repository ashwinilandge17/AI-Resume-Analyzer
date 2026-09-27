# Common job roles and their typically expected skills
# This is a predefined mapping used when a role is detected in the JD

ROLE_SKILLS_MAP = {
    "data analyst": ["python", "sql", "excel", "power bi", "tableau", "data analysis", "data visualization", "statistics"],
    "data scientist": ["python", "sql", "machine learning", "deep learning", "pandas", "numpy", "scikit-learn", "statistics"],
    "python developer": ["python", "django", "flask", "sql", "rest api", "git", "oop"],
    "web developer": ["html", "css", "javascript", "react", "node.js", "rest api", "git"],
    "backend developer": ["python", "java", "sql", "rest api", "django", "flask", "docker"],
    "frontend developer": ["html", "css", "javascript", "react", "node.js"],
    "machine learning engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn"],
    "business analyst": ["excel", "sql", "power bi", "tableau", "data analysis", "communication"],
    "software engineer": ["python", "java", "c++", "git", "data structures", "algorithms", "oop"],
}


def detect_role_and_get_skills(jd_text):
    """
    Detects a job role mentioned in the JD text
    and returns the typically expected skills for that role
    """
    jd_text_lower = jd_text.lower()

    for role, skills in ROLE_SKILLS_MAP.items():
        if role in jd_text_lower:
            return role, skills

    return None, []