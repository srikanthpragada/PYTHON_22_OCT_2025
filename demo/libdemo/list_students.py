import re

students = []
with  open("students.txt", "rt") as f:
    for line in f.readlines():
        # look for name
        match = re.search("[a-zA-Z ]+", line)
        if not match:
            continue  # ignore line

        name = match.group()

        # look for mobile
        match = re.search(r"\d+", line)
        if not match:
            continue  # ignore line

        mobile = match.group()
        if len(mobile) != 10:
            continue

        students.append( (name.strip(), mobile))


for name, mobile in sorted(students):
    print(f"{name:20}  {mobile:10}")