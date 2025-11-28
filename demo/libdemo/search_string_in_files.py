import os
import sys

if len(sys.argv) < 3:
    startdir = input("Enter starting directory:")
    search = input("Enter search string :")
else:
    startdir = sys.argv[1]
    search = sys.argv[2]

def contains(filename : str, searchstring : str)-> bool:
    try:
        with open(filename, "rt") as f:
            return  searchstring in f.read()
    except:
        return False


g = os.walk(startdir)

for (directory, folders, files) in g:
     for f in files:
         fullpath = directory + "\\" + f
         if contains(fullpath, search):
             print(fullpath)

