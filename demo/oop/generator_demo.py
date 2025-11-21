# Generator
def squares(num: int):
    for n in range(1, num + 1):
        yield n * n

g = squares(3)
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))


