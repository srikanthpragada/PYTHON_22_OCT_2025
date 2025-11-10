g = 1000   # Global
def f1():
    global g
    g = 1
    a = 100   #Enclosing
    def f2():
        nonlocal a
        a = 1
        b = 10   #Local
        print(g, a, b)

    f2()
    print(a)  #?

f1()


