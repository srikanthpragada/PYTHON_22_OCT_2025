from datetime import datetime

players = []
with open("players.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue  # Ignore line

        # convert second part to datetime
        try:
            dob = datetime.strptime(parts[1], "%d-%m-%Y")
        except:
            continue  # ignore line

        years = (datetime.now() - dob).days // 365
        players.append((parts[0], years))

for name, age in sorted(players, key=lambda t: t[1]):
    print(f"{name:15} {age:2}")
