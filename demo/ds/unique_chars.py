
names = ['Java', 'JavaScript', 'C++', 'C#', 'php']

unique_chars = set()
for name in names:
    unique_chars = unique_chars | set(name)

print(sorted(unique_chars))


