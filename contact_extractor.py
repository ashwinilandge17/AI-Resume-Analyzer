import re

def extract_contact_info(resume_text):
    """
    Extracts email and phone number from resume text
    """
    email_match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', resume_text)
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?\d{10}', resume_text)
    
    return {
        "email": email_match.group(0) if email_match else "Not found",
        "phone": phone_match.group(0) if phone_match else "Not found"
    }