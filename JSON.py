import json

json_str = '{"name": "Alice", "age": 25, "address": {"city": "Paris"}, "hobbies": ["reading", "music"]}'

data = json.loads(json_str)

complex_found = False

if isinstance(data, dict):
    for v in data.values():
        if isinstance(v, (dict, list)):
            complex_found = True
            break
elif isinstance(data, list):
    for v in data:
        if isinstance(v, (dict, list)):
            complex_found = True
            break

print("Complex object found?", complex_found)
# ----------------------
# Output
# ----------------------
# True
