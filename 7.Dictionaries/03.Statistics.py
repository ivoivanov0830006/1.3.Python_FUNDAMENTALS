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


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the
# command "statistics". Sometimes you may receive a product more than once. In that case, you have
# to add the new quantity to the existing one. When you receive the "statistics" command, print the
# following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# bread: 4                      Products in stock:
# cheese: 2                     - bread: 5
# ham: 1                        - cheese: 2
# bread: 1                      - ham: 1
# statistics	                Total Products: 3
#                               Total Quantity: 8
# ----------------------------------------------------------------------------------------
# eggs: 10                      Products in stock:
# bread: 6                      - eggs: 10
# cheese: 8                     - bread: 6
# milk: 7                       - cheese: 8
# statistics	                - milk: 7
#                               Total Products: 4
#                               Total Quantity: 31
