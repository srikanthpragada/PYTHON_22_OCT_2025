nums = [1, 3, 3, 4, 4, 5, 3, 2, 6, 8, 1, 2, 1, 1]

freq = {}   # Empty dict

for n in sorted(nums):
    count = freq.get(n, 0)
    freq[n] = count + 1

for k, v in freq.items():
    print(k, v)



