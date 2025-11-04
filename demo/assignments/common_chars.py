# Find out common chars in the given names
common = set()
first = True
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    if first:
        common = set(name)
        first = False
    else:
        common = common & set(name)

print(common)



