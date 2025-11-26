import json

with open("customers.json", "rt") as f:
    data = json.load(f)

for person in sorted(data, key=lambda x: x["age"]):
    print(f"{person["name"]:15} {person["age"]:3}")
