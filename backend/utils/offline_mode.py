import json
import os

def cache_data():
    files = ['dictionary.json', 'user_progress.json', 'history.json', 'weekly_recap.json', 'bookmarks.json']
    cache = {}
    for file in files:
        with open(os.path.join(os.path.dirname(__file__), f'../../data/{file}'), 'r') as f:
            cache[file] = json.load(f)
    return cache