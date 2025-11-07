
st = "10,20,50,40,33"
parts = st.split(",")

total = 0
for p in parts:
    total += int(p)

print(total)
