def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def domath(a, b, task):
    print(task(a, b))


domath(10, 20, add)
domath(40, 20, sub)
