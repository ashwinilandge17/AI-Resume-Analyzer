from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, jd_text):
    """
    Takes resume text and job description text,
    and calculates the similarity score between them
    """
    documents = [resume_text, jd_text]
    
    # Convert text into numerical vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate cosine similarity (between 0 and 1, higher means better match)
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    match_percentage = round(similarity_score[0][0] * 100, 2)
    return match_percentage


# Testing
if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf
    
    resume_text = extract_text_from_pdf("Ashwini.pdf")
    
    jd_text = """
    We are looking for a Python Developer with experience in Django, Flask,
    REST APIs, SQL, and Machine Learning. Knowledge of Pandas, NumPy,
    and Scikit-learn is a plus. Familiarity with Git and GitHub required.
    """
    
    score = calculate_match_score(resume_text, jd_text)
    print(f"Resume Match Score: {score}%")