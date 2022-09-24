lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
current_lose = 0

helmet_broken = 0
sword_broken = 0
shield_broken = 0
armour_broken = 0

for lost in range(lost_fights):
    is_helmet_broken = False
    is_sword_broken = False
    current_lose += 1
    if current_lose % 2 == 0:
        is_helmet_broken = True
        helmet_broken += 1
    if current_lose % 3 == 0:
        is_sword_broken = True
        sword_broken += 1
    if is_sword_broken and is_helmet_broken:
        shield_broken += 1
        if shield_broken % 2 == 0:
            armour_broken += 1
total = helmet_price * helmet_broken + sword_price * sword_broken + \
        shield_price * shield_broken + armour_price * armour_broken
print(f"Gladiator expenses: {total:.2f} aureus")
