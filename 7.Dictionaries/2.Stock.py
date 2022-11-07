products = list(input().split())
needed_products = input().split()
stock = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    stock[key] = int(value)

for product in needed_products:
    if product in stock.keys():
        quantity = stock[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
