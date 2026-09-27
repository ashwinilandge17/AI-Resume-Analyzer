import pdfplumber

def check_ats_friendliness(pdf_path):
    """
    Checks for images/tables in the resume that can confuse ATS systems
    """
    issues = []
    score = 100
    
    with pdfplumber.open(pdf_path) as pdf:
        total_images = 0
        total_tables = 0
        
        for page in pdf.pages:
            total_images += len(page.images)
            total_tables += len(page.extract_tables())
        
        if total_images > 0:
            issues.append(f"Resume contains {total_images} image(s) - ATS systems cannot read these")
            score -= 20
        
        if total_tables > 0:
            issues.append(f"Resume contains {total_tables} table(s) - some ATS systems may fail to parse these correctly")
            score -= 15
        
        page_count = len(pdf.pages)
        if page_count > 2:
            issues.append(f"Resume is {page_count} pages long - ideal length is 1-2 pages")
            score -= 10
    
    if not issues:
        issues.append("No major ATS issues found!")
    
    return {"ats_score": max(score, 0), "issues": issues}