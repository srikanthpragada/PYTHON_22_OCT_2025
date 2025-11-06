def first_digit(s):
    for ch in s:
        if ch.isdigit():
            return ch

    return None


print(first_digit('Abc123'))
print(first_digit('hello'))
