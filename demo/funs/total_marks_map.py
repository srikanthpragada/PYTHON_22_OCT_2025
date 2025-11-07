st = "10,20,50,40,ab,33"
parts = st.split(",")
# print(parts)
nums = filter(str.isdigit, parts)
total = sum(map(int, nums))
print(total)

