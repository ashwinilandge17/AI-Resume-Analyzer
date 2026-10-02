import re


def get_remark(score):
    """
    Returns a remark based on a percentage/CGPA-equivalent score
    """
    if score >= 75:
        return "Excellent 🌟"
    elif score >= 60:
        return "Good ✅"
    elif score >= 50:
        return "Average ⚠️"
    else:
        return "Below Average ❌"


def extract_percentage_near_keyword(text, keyword, window=200):
    """
    Finds a percentage value that appears shortly after a given keyword
    """
    idx = text.lower().find(keyword.lower())
    if idx == -1:
        return None

    snippet = text[idx: idx + window]
    match = re.search(r'([\d.]+)\s*%', snippet)
    if match:
        return float(match.group(1))
    return None


def extract_detailed_education(resume_text):
    """
    Extracts 10th, 12th, and Degree (CGPA/percentage) scores separately
    from the resume text, along with a remark for each level
    """
    # 10th (Class X) detection
    tenth_score = extract_percentage_near_keyword(resume_text, "(Class X)")
    if tenth_score is None:
        tenth_score = extract_percentage_near_keyword(resume_text, "10th")
    if tenth_score is None:
        tenth_score = extract_percentage_near_keyword(resume_text, "SSC")

    # 12th (Class XII) detection
    twelfth_score = extract_percentage_near_keyword(resume_text, "(Class XII)")
    if twelfth_score is None:
        twelfth_score = extract_percentage_near_keyword(resume_text, "12th")
    if twelfth_score is None:
        twelfth_score = extract_percentage_near_keyword(resume_text, "HSC")

    # Degree (CGPA or percentage) detection
    cgpa_match = re.search(r'CGPA[:\s]*([\d.]+)', resume_text, re.IGNORECASE)
    if cgpa_match:
        degree_score = float(cgpa_match.group(1)) * 10
    else:
        degree_score = extract_percentage_near_keyword(resume_text, "B.Tech")

    return {
        "tenth": {
            "score": tenth_score,
            "remark": get_remark(tenth_score) if tenth_score is not None else "Not found"
        },
        "twelfth": {
            "score": twelfth_score,
            "remark": get_remark(twelfth_score) if twelfth_score is not None else "Not found"
        },
        "degree": {
            "score": degree_score,
            "remark": get_remark(degree_score) if degree_score is not None else "Not found"
        }
    }


def extract_education_score(resume_text):
    """
    Extracts CGPA and Percentage from resume text
    and returns an overall average education score with a remark
    """
    result = {
        "cgpa_found": None,
        "percentage_found": [],
        "education_remark": ""
    }

    cgpa_match = re.search(r'CGPA[:\s]*([\d.]+)', resume_text, re.IGNORECASE)
    if cgpa_match:
        result["cgpa_found"] = float(cgpa_match.group(1))

    percentage_matches = re.findall(r'([\d.]+)\s*%', resume_text)
    result["percentage_found"] = [float(p) for p in percentage_matches]

    scores = []
    if result["cgpa_found"] is not None:
        scores.append(result["cgpa_found"] * 10)
    scores.extend(result["percentage_found"])

    if scores:
        avg_score = sum(scores) / len(scores)
        result["education_remark"] = get_remark(avg_score)
        result["average_academic_score"] = round(avg_score, 2)
    else:
        result["education_remark"] = "Education details not found"
        result["average_academic_score"] = 0

    return result


# Testing
if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf

    resume_text = extract_text_from_pdf("Ashwini.pdf")
    edu_result = extract_education_score(resume_text)
    detailed = extract_detailed_education(resume_text)

    print("Average Score:", edu_result["average_academic_score"])
    print("10th:", detailed["tenth"])
    print("12th:", detailed["twelfth"])
    print("Degree:", detailed["degree"])
    