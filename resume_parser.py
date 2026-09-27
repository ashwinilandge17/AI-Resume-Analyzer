import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Takes a PDF file path and returns
    the complete extracted text from it
    """
    full_text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # if text was found on the page
                full_text += text + "\n"
    
    return full_text


# For testing purposes (runs only when this file is executed directly)
if __name__ == "__main__":
    sample_resume_path = "Ashwini.pdf"
    result = extract_text_from_pdf(sample_resume_path)
    print(result)