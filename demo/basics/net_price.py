# Take price and display net price after discount

price = int(input("Enter price :"))

if price > 10000:
    discount = price * 20 // 100
elif price > 5000:
    discount = price * 10 // 100
else:
    discount = price * 5 // 100

net_price = price - discount
print(f'Base Price  : {price:6}')
print(f'Discount    : {discount:6}')
print(f'Net Price   : {net_price:6}')


