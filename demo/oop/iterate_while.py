l = [1, 2, 3, 4]

for n in l:
    print(n)

li = iter(l) # l.__iter__()
while True:
    try:
        print(next(li))   # li.__next__()
    except:
        break


print(dir(li))