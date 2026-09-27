import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"

def save_to_history(filename, overall_match, skill_match, academic_score):
    history = load_history()
    history.append({
        "filename": filename,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "overall_match": overall_match,
        "skill_match": skill_match,
        "academic_score": academic_score
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []