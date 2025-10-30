# Accept a string and display if it's valid mobile number or not
st = input("Enter mobile number: ")
if len(st) == 10 and st.isdigit():
    print(st, " is a valid mobile number.")
else:
    print(st, " is not a valid mobile number.")