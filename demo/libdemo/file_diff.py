# Compare files by lines
filename1 = "names.txt"
filename2 = "names2.txt"

with open(filename1, "rt") as f1, open(filename2, "rt") as f2:
    lineno = 1
    while True:
        line1 = f1.readline()
        line2 = f2.readline()

        if line1 != line2:
            print(f'Differ at line number : {lineno}')
            break

        if line1 == "":  # EOF
            print('No difference. Files are same!')
            break

        lineno += 1


