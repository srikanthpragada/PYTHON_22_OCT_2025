# Take all uppercase letter first and then lowercase letters and
# create a string from all those characters

st = "How DO you DO"

upper = []
lower = []

for c in st:
    if c.isupper():
        upper.append(c)
    elif c.islower():
        lower.append(c)

print(upper + lower)
print( "".join( upper + lower))
