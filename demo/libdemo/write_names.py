
names = ['Andy', 'Mark', 'Scott', 'Jason', 'Carlton']
f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()

