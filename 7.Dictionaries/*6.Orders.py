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
