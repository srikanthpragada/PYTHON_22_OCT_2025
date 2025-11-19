total = 0
while True:
    try:
        num = int(input("Enter number [0 to stop]: "))
        if num == 0:
            break
        total += num
    except:
        print('Invalid Number!')

print(f"Total = {total}")
