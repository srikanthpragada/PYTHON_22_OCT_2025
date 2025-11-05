
def smallest_factor(num):
    for n in range(2, num//2 + 1):
        if  num % n == 0:
            return n

    # when num is prime, itself is the smallest factor
    return num


print(smallest_factor(45), smallest_factor(59))
