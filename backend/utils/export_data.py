import json
import os

def export_progress(user_id):
    progress = os.path.join(os.path.dirname(__file__), '../../data/user_progress.json')
    with open(progress, 'r') as f:
        data = json.load(f)
    with open(f"{user_id}_progress.json", 'w') as f:
        json.dump(data.get(user_id, {}), f, indent=4)
    return f"{user_id}_progress.json"