food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
everything_enough = True

food_per_day = 0.3

for day in range(1, 31):
    food -= food_per_day
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        everything_enough = False
        break

if everything_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
    

# ----------------------------------- Problem to resolve -----------------------------
#
# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for
# a month (30 days). On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain
# amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a
# quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
#   * On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
#   * On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
#   * On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
#   * On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
# Output
#   * If the food, the hay, and the cover are enough, print:
#       "Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
#   * If one of the things is not enough, print:
#       "Merry must go to the pet store!"
# The output values must be formatted to the second decimal place!
# Input	                Output
# 10                    Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87.
# 5
# 5.2
# 1
# --------------------------------------------------------------------------------------------
# 1                     Merry must go to the pet store!
# 1.5
# 3
# 1.5
# --------------------------------------------------------------------------------------------
# 9                     Merry must go to the pet store!
# 5
# 5.2
# 1
