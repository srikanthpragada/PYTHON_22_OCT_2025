nums = [1, 3, 3, 4, 4, 5, 3, 2, 6, 8, 1, 2, 1, 1]

for n in sorted(set(nums)):
    print(n, nums.count(n))
