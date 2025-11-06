def print_uppercase_reverse(str):
    for c in str[::-1]:
        if c.isupper():
           print(c, end = '')


print_uppercase_reverse('AbC123Xyz')