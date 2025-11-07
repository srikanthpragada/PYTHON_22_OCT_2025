def next_even(n):
    return  n if n % 2 == 0 else n + 1

nums = [10, 21, 43, 50, 80]

for v in map(next_even, nums):
    print(v)
