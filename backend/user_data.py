import json
import os

def save_progress(user_id, word):
    progress_file = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')
    history_file = os.path.join(os.path.dirname(__file__), '../data/history.json')
    
    # Update progress
    with open(progress_file, 'r+') as f:
        data = json.load(f)
        if user_id not in data:
            data[user_id] = {"words": [], "scores": []}
        if word not in data[user_id]["words"]:
            data[user_id]["words"].append(word)
        f.seek(0)
        json.dump(data, f, indent=4)
    
    # Update history
    with open(history_file, 'r+') as f:
        history = json.load(f)
        if user_id not in history:
            history[user_id] = []
        history[user_id].append({"word": word, "timestamp": "2025-03-25"})
        f.seek(0)
        json.dump(history, f, indent=4)

def get_progress(user_id):
    with open(os.path.join(os.path.dirname(__file__), '../data/user_progress.json'), 'r') as f:
        data = json.load(f)
        return data.get(user_id, {"words": [], "scores": []})

def get_history(user_id):
    with open(os.path.join(os.path.dirname(__file__), '../data/history.json'), 'r') as f:
        history = json.load(f)
        return history.get(user_id, [])