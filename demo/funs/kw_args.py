def show(**kwargs):
    print(kwargs)

def details(*args, **kwargs):
    pass

show(a = 10, x = 20, name = 'Srikanth')
details(10, 20, x = 1, y = 2)

