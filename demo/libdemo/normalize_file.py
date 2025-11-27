import re

filename = "test.txt"

with open(filename, "rt") as f:
    contents = f.read()

new_contents = re.sub(r' +', ' ', contents)
new_contents = re.sub('\n+', '\n', new_contents)

print(new_contents)

# with open(filename, "wt") as f:
#     f.write(new_contents)
