import os

f = open("names.txt", "rt")
print(f'Open in {f.mode} mode')
for n in f.readlines():
    print(n.strip())

print("File Pointer Position :", f.tell())

f.seek(0, os.SEEK_SET)   # reposition file pointer to the beginning of the file
print(f.read())

f.close()

