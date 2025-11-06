# Create a function that takes 2 numbers and print common factors.

def common_factors(num1, num2):
    smallest = min(num1, num2)
    for i in range(2, smallest // 2 + 1):
        if num1 % i == 0 & num2 % i == 0:
            print(i)


common_factors(27, 900)
