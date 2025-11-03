
names = ['Java', 'JavaScript', 'C++', 'C#', 'php']

unique_chars = []
for name in names:
    for ch in name:
        if ch not in unique_chars:
            unique_chars.append(ch)

print(unique_chars)


