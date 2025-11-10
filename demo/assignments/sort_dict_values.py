
d = { 1: 10, 5 : 5, 3 : 20, 2 : 200}

for v in sorted(d.items(), key = lambda t: t[1]):
    print(v)
