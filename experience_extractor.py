import re

def extract_experience(resume_text):
    """
    Searches for patterns like '2 years', '1.5 years' in resume text
    and returns the highest number found
    """
    matches = re.findall(r'(\d+\.?\d*)\+?\s*years?', resume_text, re.IGNORECASE)
    
    if matches:
        years = [float(m) for m in matches]
        return max(years)
    return 0