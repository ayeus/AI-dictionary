import json
import os

def cache_data():
    with open(os.path.join(os.path.dirname(__file__), '../../data/dictionary.json'), 'r') as f:
        return json.load(f)