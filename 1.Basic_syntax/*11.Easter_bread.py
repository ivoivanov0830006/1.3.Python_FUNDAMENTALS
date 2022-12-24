budget = float(input())
flour_price_kg = float(input())
eggs_price_pack = 0.75 * flour_price_kg
milk_price_liter = 1.25 * flour_price_kg
loaf_price = flour_price_kg + eggs_price_pack + milk_price_liter / 4
loaf_count = 0
colored_eggs = 0

while budget > loaf_price:
    budget -= loaf_price
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= (loaf_count - 2)
print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and"
      f" {budget:.2f}BGN left.")


# ------------------------------------- Problem to resolve ------------------------------
#
# Create a program that calculates how many loaves you can make (according to the recipe)
# with the budget you have. Here is the recipe for one loaf:
#           Eggs	1 pack
#           Flour	1 kg
#           Milk	0.250 l
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1L milk is
# 25% more than the price for 1 kg flour. Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
#   - For every loaf of bread that you make, you will receive 3 colored eggs.
#   - For every 3rd bread you make, you will lose some of your colored eggs after receiving
#     the usual 3 colored eggs for your bread. The count of eggs you will lose is calculated
#     when you subtract 2 from your current count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left,
# formatted to the 2nd decimal place, in the following format:
#   - "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs
#      and {money_left}BGN left."
# Input / Constraints
#   - On the 1st line, you will receive the budget - a real number in the range [0.0…100000.0]
#   - On the 2nd line, you will receive the price for 1 kg flour - a real number in the range [0.0…100000.0]
#   - The input will always be in the correct format
#   - You will always have a remaining budget
#   - There will not be a case in which the eggs become a negative count
# Output
#   - In the end, print the number of loaves of Easter bread you have made, the colored eggs you
#     have gathered, and the money formatted to the 2nd decimal place in the format described above.
# -------------------------------------- Example inputs ----------------------------------
# Input	            Output
# 20.50
# 1.25	            You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.
# ------------------------------------------------------------------------------------------
# 15.75
# 1.4	            You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.
