# No overloading of functions

def add(a, b):
    return a + b

print(add(10,20))

def add(a, b, c):
    return a + b + c


#print(add(10, 20))
print(add(10, 20, 30))
