SKILL_SUGGESTIONS = {
    "docker": "Learn containerization basics and practice by deploying a small project using Docker.",
    "kubernetes": "Strengthen your Docker skills first, then learn basic pod/deployment concepts.",
    "react": "Build a small frontend project (like a to-do app) by following the official React docs.",
    "fastapi": "FastAPI is easier to learn than Flask — build a REST API by following the official tutorial.",
    "postgresql": "Practice basic SQL queries and build a small CRUD project using PostgreSQL.",
    "excel": "Practice basic formulas, pivot tables, and VLOOKUP.",
}

def generate_suggestions(missing_skills):
    """
    Generates improvement suggestions for each missing skill
    """
    suggestions = []
    for skill in missing_skills:
        if skill in SKILL_SUGGESTIONS:
            suggestions.append(f"**{skill.title()}**: {SKILL_SUGGESTIONS[skill]}")
        else:
            suggestions.append(f"**{skill.title()}**: You can learn the basics from free YouTube tutorials or official docs.")
    return suggestions