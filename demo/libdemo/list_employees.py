f = open("employees.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 3:
        continue

    dept = parts[0]
    names = parts[1::2]
    salaries = parts[2::2]

    employees = list(zip(names, salaries))
    # print(employees)
    print(dept)
    print("=" * 10)
    for name, salary in sorted(employees):
        print(f"{name:20} {salary:6}")

f.close()
