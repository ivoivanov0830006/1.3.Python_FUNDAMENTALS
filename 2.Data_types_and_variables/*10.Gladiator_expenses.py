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


# --------------------------- Problem to resolve ----------------------------

# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and an armor. You will receive
# Peter's lost fights count.
#   - Every second lost game, his helmet is broken.
#   - Every third lost game, his sword is broken.
#   - When both his sword and helmet are broken in the same lost fight, his shield also breaks.
#   - Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year
# for renewing his equipment.
# The input will consist of 5 lines:
#   - On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
#   - On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
#   - On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
#   - On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
#   - On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
#   - As output, you must print Peter`s total expenses for new equipment:
#           "Gladiator expenses: {expenses} aureus"
# Input	                Output	                            Comment
# 7                     Gladiator expenses: 16.00 aureus	Trashed helmet -> 3 times
# 2                                                         Trashed sword -> 2 times
# 3                                                         Trashed shield -> 1 time
# 4                                                         Total: 6 + 6 + 4 = 16.00 aureus;
# 5
# -------------------------------------------------------------------------------------------
# 23                    Gladiator expenses: 608.00 aureus
# 12.50
# 21.50
# 40
# 200
