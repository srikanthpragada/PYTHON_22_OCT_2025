
marks = [10, 23,33,22, 50]

try:
    rollno = int(input("Enter rollno:"))
    print('Marks :', marks[rollno - 1])
except ValueError:
    print("Invalid number!")
else:
    print("Success")
finally:
    print('Finally!')

print("The End!")


