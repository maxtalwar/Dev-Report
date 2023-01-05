import json

def save_cache_to_json(cache, filename):
    with open(filename, 'w') as f:
        json.dump(cache, f, indent=2)

def load_cache_from_json(filename):
    with open(filename, 'r') as f:
        cache = json.load(f)
    return cache

