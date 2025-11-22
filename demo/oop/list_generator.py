import sys

# Generator
g = (n * n for n in range(1, 11))
print(sys.getsizeof(g))
for n in g:
    print(n, end=' ')

print()
# List
l = [n * n for n in range(1, 11)]
print(sys.getsizeof(l))
for n in l:
    print(n, end=' ')
