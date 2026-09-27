import re

def extract_education_score(resume_text):
    """
    Extracts CGPA and Percentage from resume text
    and returns an education score with a remark
    (Excellent / Good / Average / Below Average)
    """
    result = {
        "cgpa_found": None,
        "percentage_found": [],
        "education_remark": ""
    }
    
    # Search for CGPA (e.g. "CGPA: 7.55" or "CGPA 7.55")
    cgpa_match = re.search(r'CGPA[:\s]*([\d.]+)', resume_text, re.IGNORECASE)
    if cgpa_match:
        cgpa_value = float(cgpa_match.group(1))
        result["cgpa_found"] = cgpa_value
    
    # Search for percentages (e.g. "62.33%" or "82.60%")
    percentage_matches = re.findall(r'([\d.]+)\s*%', resume_text)
    result["percentage_found"] = [float(p) for p in percentage_matches]
    
    # Now decide the score/remark
    scores = []
    
    if result["cgpa_found"] is not None:
        # CGPA is usually on a 10-point scale
        cgpa_percent_equivalent = result["cgpa_found"] * 10  # rough conversion
        scores.append(cgpa_percent_equivalent)
    
    scores.extend(result["percentage_found"])
    
    if scores:
        avg_score = sum(scores) / len(scores)
        
        if avg_score >= 75:
            remark = "Excellent 🌟"
        elif avg_score >= 60:
            remark = "Good ✅"
        elif avg_score >= 50:
            remark = "Average ⚠️"
        else:
            remark = "Below Average ❌"
        
        result["education_remark"] = remark
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
    
    print("CGPA Found:", edu_result["cgpa_found"])
    print("Percentages Found:", edu_result["percentage_found"])
    print("Average Academic Score:", edu_result["average_academic_score"])
    print("Remark:", edu_result["education_remark"])