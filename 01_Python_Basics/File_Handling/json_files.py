import json
with open("simple_user.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)