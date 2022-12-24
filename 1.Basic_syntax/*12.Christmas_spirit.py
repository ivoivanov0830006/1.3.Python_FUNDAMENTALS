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


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that calculates how much money you will need to spend on Christmas
# decorations and how much your Christmas spirit will improve.
#   - On the first line, you will receive the quantity of decorations you should buy each time you go shopping.
#   - On the second line, you will receive the days left until Christmas.
# There are 4 types of decorations, and each piece costs a certain price.
# Also, each time you go shopping for a concrete type of decoration, your Christmas spirit is improved by some points:
#   Decoration	    Price/Piece	Points/Shopping
#  Ornament Set	        2$	            5
#   Tree Skirt	        5$	            3
#  Tree Garland	        3$	            10
#  Tree Lights	        15$         	17
# Until Christmas, you go shopping for a certain decoration as follows:
#   - Every second day you buy Ornament Sets.
#   - Every third day you buy Tree Skirts and Tree Garlands.
#   - Every fifth day you buy Tree Lights.
# If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30.
# That's not all! You have a cat at home that really likes to mess around with the decoration:
# Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
# Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt,
# garlands, and lights, but you do NOT earn additional spirit points for them.
# Also, because of the cat - at the beginning of every eleventh day, you are forced to increase
# the quantity of decorations needed to be bought each time you go shopping by 2.
# If the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey,
# and you lose an additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.
# Input / Constraints
# The input will consist of exactly 2 lines:
#   - quantity - integer in the range [1…100]
#   - days - integer in the range [1…100]
# Output
#   - In the end, print the total cost and the total gained spirit in the following format:
#   - "Total cost: {budget}"
#   - "Total spirit: {totalSpirit}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# 1                                 Total cost: 37
# 7	                                Total spirit: 58
# ------------------------------------------------------
# 3                                 Total cost: 558
# 20	                            Total spirit: 156
