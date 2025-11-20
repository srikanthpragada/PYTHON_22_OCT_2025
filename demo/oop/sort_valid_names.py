
def validate_name(name : str):
    for c in name:
        if not (c.isalpha() or c.isspace()):
            raise ValueError('Invalid Name')


names = []
while True:
    name = input("Enter name [end to stop] :").strip()
    if name.lower() == 'end':
        break
    try:
         validate_name(name)
         names.append(name)
    except ValueError:
         print('Sorry! Invalid Name!')


for name in sorted(names):
    print(name, end = ' ')
