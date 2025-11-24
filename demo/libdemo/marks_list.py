# Display student name, total marks, avg. marks

f = open("marks.txt", "rt")
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # Ignore line with insufficient data

    name = parts[0]
    marks = [int(m) for m in parts[1:] if m.isdigit()]
    total = sum(marks)
    avg = total / len(marks)

    print(f'{name:20} {total:3}  {avg:5.2f}')

f.close()
