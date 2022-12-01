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


# ------------------------------------- Another Solution -----------------------------
#
# import re
# products = {}
#
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#
#     pattern = r"^>>(?P<item>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)"
#     items = re.findall(pattern, command)
#     if items:
#         for item in items:
#             key = item[0]
#             value = float(item[1]) * int(item[2])
#             products[key] = value
#
# print("Bought furniture:")
# for product in products.keys():
#     print(f"{product}")
# print(f"Total money spend: {sum(products.values()):.2f}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that calculates the total cost of bought furniture. You will be given information about each
# purchase on separate lines until you receive the command "Purchase". Valid information should be in the
# format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# >>Sofa<<312.23!3              Bought furniture:
# >>TV<<300!5                   Sofa
# >Invalid<<!5                  TV
# Purchase	                    Total money spend: 2436.69
