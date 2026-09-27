# 📄 AI Resume Analyzer

An AI-powered resume analysis tool that evaluates resumes against job descriptions using NLP and machine learning techniques. Built with Python and Streamlit.

## 🚀 Features

- **PDF Text Extraction** — Extracts text content from uploaded resume PDFs
- **Skill Matching** — Detects 35+ technical skills from resume text using keyword matching
- **JD Similarity Score** — Calculates resume-to-job-description similarity using TF-IDF and Cosine Similarity
- **Skill-Based Match %** — Compares resume skills against job description requirements
- **Matched vs Missing Skills** — Clearly highlights which required skills are present or missing
- **Education/CGPA Analysis** — Extracts CGPA and percentages, generates an academic score
- **Contact Info Extraction** — Automatically detects email and phone number
- **Experience Detection** — Identifies years of experience mentioned in the resume
- **ATS Friendliness Check** — Flags resume formatting issues (images, tables, page count) that can affect ATS parsing
- **Improvement Suggestions** — Provides learning suggestions for missing skills
- **Skill Match Visualization** — Pie chart showing matched vs missing skills
- **Multiple Resume Support** — Upload and compare multiple resumes against one job description, with ranking
- **PDF Report Generation** — Download a complete analysis report as a PDF
- **Analysis History** — Tracks previously analyzed resumes

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Web interface
- **pdfplumber** — PDF text extraction
- **scikit-learn** — TF-IDF vectorization and cosine similarity
- **spaCy** — NLP processing
- **fpdf2** — PDF report generation
- **matplotlib** — Data visualization
- **pandas** — Data handling

## 📸 How It Works

1. Upload one or more resumes (PDF format)
2. Paste the job description you're comparing against
3. Click "Analyze Resume(s)"
4. View detailed results: match scores, skill breakdown, education analysis, ATS check, and suggestions
5. Download a PDF report of the analysis

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
```

4. Run the app:
```bash
   streamlit run app.py
```

## 📂 Project Structure
resume-analyzer/
├── app.py # Main Streamlit application
├── resume_parser.py # PDF text extraction
├── skills_list.py # Predefined skills database
├── skill_matcher.py # Skill detection and comparison logic
├── jd_matcher.py # TF-IDF based similarity scoring
├── education_matcher.py # CGPA/percentage extraction and scoring
├── contact_extractor.py # Email and phone extraction
├── experience_extractor.py # Years of experience detection
├── ats_checker.py # ATS friendliness analysis
├── suggestions.py # Skill improvement suggestions
├── history_manager.py # Analysis history tracking
├── report_generator.py # PDF report generation
└── requirements.txt


## 👤 Author

**Ashwini Prakash Landge**
Python Developer | B.Tech CSE (AI & ML)
📧 landgeashwini36@gmail.com