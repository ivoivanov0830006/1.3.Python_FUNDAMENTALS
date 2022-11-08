orders = {}

while True:
    command = input().split(" ")
    if command[0] == "buy":
        break
    product, price, quantity = command[0], float(command[1]), int(command[2])
    if product not in orders.keys():
        orders[product] = []
        orders[product].append(price)
        orders[product].append(quantity)

    else:
        orders[product].insert(0, price)
        orders[product].pop(1)
        previous_quantity = orders[product].pop(1)
        orders[product].append(quantity + previous_quantity)
        total = orders[product][0] * orders[product][1]

for key, value in orders.items():
    value = value[0] * value[1]
    print(f"{key} -> {value:.2f}")

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that keeps the information about products and their prices. Each product has a name,
# a price, and a quantity:
#   If the product doesn't exist yet, add it with its starting quantity.
#   If you receive a product, which already exists, increases its quantity by the input quantity and if
# its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command
# "buy", keep adding items. Finally, print all items with their names and the total price of each product.
# Input
# Until you receive "buy", the products will be coming in the format:
#       "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
#       "{product_name} -> {total_price}"
# Format the total price to the 2nd digit after the decimal separator.
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# Beer 2.20 100                     Beer -> 220.00
# IceTea 1.50 50                    IceTea -> 75.00
# NukaCola 3.30 80                  NukaCola -> 264.00
# Water 1.00 500                    Water -> 500.00
# buy
# --------------------------------------------------------
# Beer 2.40 350                     Beer -> 660.00
# Water 1.25 200                    Water -> 250.00
# IceTea 5.20 100                   IceTea -> 110.00
# Beer 1.20 200
# IceTea 0.50 120
# buy
# --------------------------------------------------------
# CesarSalad 10.20 25               CesarSalad -> 255.00
# SuperEnergy 0.80 400              SuperEnergy -> 320.00
# Beer 1.35 350                     Beer -> 472.50
# IceCream 1.50 25                  IceCream -> 37.50
# buy
