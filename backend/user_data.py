import json
import os
from datetime import datetime

def save_progress(user_id, word):
    progress_file = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')
    history_file = os.path.join(os.path.dirname(__file__), '../data/history.json')
    recap_file = os.path.join(os.path.dirname(__file__), '../data/weekly_recap.json')
    
    # Update progress
    with open(progress_file, 'r+') as f:
        data = json.load(f)
        if user_id not in data:
            data[user_id] = {"words": [], "scores": [], "bookmarks": []}
        if word not in data[user_id]["words"]:
            data[user_id]["words"].append(word)
        f.seek(0)
        json.dump(data, f, indent=4)
    
    # Update history
    with open(history_file, 'r+') as f:
        history = json.load(f)
        if user_id not in history:
            history[user_id] = {"words": [], "quizzes": [], "activities": []}
        history[user_id]["words"].append({"word": word, "timestamp": datetime.now().strftime("%Y-%m-%d")})
        f.seek(0)
        json.dump(history, f, indent=4)

    # Update weekly recap
    week = datetime.now().strftime("week_%W_%Y")
    with open(recap_file, 'r+') as f:
        recap = json.load(f)
        if week not in recap:
            recap[week] = {"words": [], "quiz_scores": []}
        if word not in recap[week]["words"]:
            recap[week]["words"].append(word)
        f.seek(0)
        json.dump(recap, f, indent=4)

def save_bookmark(user_id, word):
    bookmark_file = os.path.join(os.path.dirname(__file__), '../data/bookmarks.json')
    with open(bookmark_file, 'r+') as f:
        bookmarks = json.load(f)
        if user_id not in bookmarks:
            bookmarks[user_id] = []
        if word not in bookmarks[user_id]:
            bookmarks[user_id].append(word)
        f.seek(0)
        json.dump(bookmarks, f, indent=4)

def get_progress(user_id):
    with open(os.path.join(os.path.dirname(__file__), '../data/user_progress.json'), 'r') as f:
        return json.load(f).get(user_id, {"words": [], "scores": []})

def get_history(user_id):
    with open(os.path.join(os.path.dirname(__file__), '../data/history.json'), 'r') as f:
        return json.load(f).get(user_id, {"words": [], "quizzes": [], "activities": []})

def get_bookmarks(user_id):
    with open(os.path.join(os.path.dirname(__file__), '../data/bookmarks.json'), 'r') as f:
        return json.load(f).get(user_id, [])