with open('names.txt', 'rt') as f:
    lines = f.readlines()

with open("names.txt", 'wt') as f:
    for line in filter(lambda l: len(l.strip()) > 0, lines):
        f.write(line)
