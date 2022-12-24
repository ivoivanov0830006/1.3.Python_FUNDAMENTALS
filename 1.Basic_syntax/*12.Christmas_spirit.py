ornament_price = 2
ornament_spirit = 5
tree_lights_price = 15
tree_lights_spirit = 17
tree_garland_price = 3
tree_garland_spirit = 10
tree_skirt_price = 5
tree_skirt_spirit = 3

spirit = 0
budget = 0

quantity = int(input())
days = int(input())

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_price * quantity
        spirit += ornament_spirit
    if day % 3 == 0:
        budget += (tree_skirt_price + tree_garland_price) * quantity
        spirit += tree_skirt_spirit + tree_garland_spirit
    if day % 5 == 0:
        budget += tree_lights_price * quantity
        spirit += tree_lights_spirit
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        budget += tree_skirt_price + tree_garland_price + tree_lights_price
        spirit -= 20
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
