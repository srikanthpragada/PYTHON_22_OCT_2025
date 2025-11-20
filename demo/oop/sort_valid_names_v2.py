def validate_name(name: str) -> bool:
    for c in name:
        if not (c.isalpha() or c.isspace()):
            return False
    return True


names = []
while True:
    name = input("Enter name [end to stop] :").strip()
    if name.lower() == 'end':
        break
    if validate_name(name):
        names.append(name)
    else:
        print('Sorry! Invalid Name!')

for name in sorted(names):
    print(name, end=' ')
