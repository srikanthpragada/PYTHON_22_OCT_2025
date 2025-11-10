# Filter demo

def ispositive(n : int) -> bool:
    return n > 0


nums = [10, -10, 4, -5, -9, 20]

for n in filter(ispositive, nums):
    print(n)

for c in filter(str.isupper, "AbXyZ"):
    print(c)
