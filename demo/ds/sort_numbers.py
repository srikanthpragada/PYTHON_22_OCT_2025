
# Take numbers from user until 0 is given and then sort them

nums = []   # Empty list

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    nums.append(num)

nums.sort()

print(nums)
