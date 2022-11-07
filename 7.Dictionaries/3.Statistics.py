products = {}

command = input()

while command != "statistics":
    product, quantity = command.split(": ")

    if product not in products:
        products[product] = 0
    products[product] += int(quantity)
    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
