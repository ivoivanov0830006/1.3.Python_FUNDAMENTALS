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


# ------------------------------------- Another Solution -----------------------------
#
# statistics = {}
#
# while True:
#     command = input()
#     if command == "statistics":
#         break
#     current_command = command.split(": ")
#     food = current_command[0]
#     pieces = int(current_command[1])
#
#     if food not in statistics.keys():
#         statistics[food] = 0
#     statistics[food] += pieces
#
# print("Products in stock:")
# for product, quantity in statistics.items():
#     print(f"- {product}: {quantity}")
# print(f"Total Products: {len(statistics.items())}")
# print(f"Total Quantity: {sum(statistics.values())}")
