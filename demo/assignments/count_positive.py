def count_positives(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1

    return count


print(count_positives([-10, -5, 6, 8, 0]))
