import os

startdir = r"c:\classroom\oct22\demo"
g = os.walk(startdir)
totalcount = 0
for (dirname, folders, files) in  g:
    print(dirname)
    count = 0
    for f in files:
        if f.endswith('.py'):
            print(' ' * 5,f)
            count += 1

    print(f'Count = {count}')
    totalcount += count


print(f'Total Count : {totalcount}')



