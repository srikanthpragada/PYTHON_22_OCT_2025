total = count = 0
while True:
    try:
        num = int(input("Enter number [0 to stop]: "))
        if num == 0:
            break
        total += num
        count += 1
        if count == 5:
            break
    except:
        print('Invalid Number!')

print(f"Total = {total}")
