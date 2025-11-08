def extract_upper(s):
    return "".join(filter(str.isupper, s))


# print(extract_upper('AbcXyz'))

names = ['Billy Joel', 'Bruce Sprignsteen', 'U2', 'Micheal Jackson']

for n in map(extract_upper, names):
    print(n)
