from spellchecker import SpellChecker
import re


def check_spelling(resume_text):
    """
    Checks resume text for potentially misspelled words using a
    dictionary-based spell checker. Skips common technical terms,
    names, and place names so they are not incorrectly flagged.
    """
    spell = SpellChecker()

    words = re.findall(r"[A-Za-z]+", resume_text)
    words = [w for w in words if len(w) > 2]

    known_extra_words = [
        "python", "django", "flask", "sql", "html", "css", "pandas",
        "numpy", "scikit", "matplotlib", "streamlit", "fastapi", "api",
        "cgpa", "linkedin", "github", "pdf", "nlp", "xii", "eda",
        "sqlite", "mysql", "oop", "pycharm", "backend", "frontend",
        "colab", "yfinance", "tensorflow", "pytorch", "npm",
        "json", "csv", "sdk", "ide", "cli", "ui", "ux"
    ]
    spell.word_frequency.load_words(known_extra_words)

    misspelled = spell.unknown(words)

    # Skip very short flagged words (often false positives like abbreviations)
    filtered = [w for w in misspelled if len(w) > 3]

    return filtered[:15]