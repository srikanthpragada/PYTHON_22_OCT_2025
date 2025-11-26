# Remove blanks from Names1.txt and store it in Temp.txt. Delete Names1.txt and rename Temp.txt as Names1.txt
import os

with open("Names.txt", "rt") as sf, open("Temp.txt", "wt") as tf:
    while True:
        line = sf.readline()
        if len(line) == 0:  # EOF
            break
        if len(line.strip()) > 0:  # if not blank line
            tf.write(line)

os.remove("Names.txt")
os.rename("Temp.txt", "Names.txt")
