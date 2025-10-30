
# Take names from user until end is given and then sort them

names = []   # Empty list

while True:
    name = input("Enter a name[end to stop] :")
    if name.lower() == 'end':
        break

    names.append(name)

names.sort()

print(names)
