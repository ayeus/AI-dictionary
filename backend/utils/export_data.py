import json
import os

def export_progress(user_id):
    progress_file = os.path.join(os.path.dirname(__file__), '../../data/user_progress.json')
    with open(progress_file, 'r') as f:
        data = json.load(f)
    export_file = f"{user_id}_progress.json"
    with open(export_file, 'w') as f:
        json.dump(data.get(user_id, {}), f, indent=4)
    return export_file