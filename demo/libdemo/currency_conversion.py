import requests

code = input("Enter currency code :")
amount = float(input("Enter amount :"))

resp = requests.get(f"https://api.exchangerate-api.com/v4/latest/{code}")
details = resp.json()
rate = details['rates']['INR']
inr = amount * rate
print(f"{amount} in {code} = {inr:10.2f} in INR")
