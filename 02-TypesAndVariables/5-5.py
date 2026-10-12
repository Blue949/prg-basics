price = input("Enter price: ")
discount = input("Enter discount: ")
price = float(price)
discount = float(discount)

print(f"Price with discount: {round(price - price*discount/100, 2)}")
print(f"Reduction: {round(price-round(price - price*discount/100, 2), 2)}")