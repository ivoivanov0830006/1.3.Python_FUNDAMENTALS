items = input().split("|")
budget = float(input())
starting_budget = budget

inventory = []

for item in items:
    item_data = item.split("->")
    item_type = item_data[0]
    item_price = float(item_data[1])
    if item_type == "Clothes":
        if item_price <= 50:
            budget -= item_price
            inventory.append(item_price * 1.4)
    elif item_type == "Shoes":
        if item_price <= 35:
            budget -= item_price
            inventory.append(item_price * 1.4)
    elif item_type == "Clothes":
        if item_price <= 20.5:
            budget -= item_price
            inventory.append(item_price * 1.4)
sum_inventory = sum(inventory)
final_inventory = ['%.2f' % elem for elem in inventory]
string_inventory = list(map(str, final_inventory))
print(" ".join(string_inventory))

print(f"Profit: {(sum_inventory - starting_budget + budget):.2f}")
total_money = sum_inventory + budget
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
