import re
products = []
total_sum = 0

while True:
    command = input()
    if command == "Purchase":
        break

    pattern = r"^>>(?P<item>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)"
    items = re.search(pattern, command)

    if items:
        furniture, price, quantity = items.groups()
        products.append(furniture)
        total_sum += float(price) * int(quantity)

print("Bought furniture:")
for product in products:
    print(f"{product}")
print(f"Total money spend: {total_sum:.2f}")