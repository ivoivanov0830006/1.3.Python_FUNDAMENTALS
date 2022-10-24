days = int(input())
players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_food = days * food_per_day * players
total_water = days * water_per_day * players

previous_water = 0
previous_food = 0

no_energy = False

for day in range(1, days + 1):
    previous_water = total_water
    previous_food = total_food
    energy_loss = float(input())
    group_energy -= energy_loss

    if day % 2 == 0:  # (watering day)
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:  # (eating day)
        group_energy += group_energy * 0.1
        total_food -= total_food / players
    if group_energy <= 0:
        no_energy = True
        break

if no_energy:
    print(f"You will run out of energy. You will be left with {previous_food:.2f} food and {previous_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that calculates the needed provision for a quest in the woods.
# First you will receive the days of the adventure, the count of the players and the group's
# energy. Afterward you will receive provision for a day for one person:
#           * Water
#           * Food
# The group calculates how many supplies they'd need for the adventure and takes that much water
# and food.
#   * Every day they chop wood an lose certain amount of energy. For each of the days you are going
# to receive the amount of energy lost from chopping wood. The program should end if the energy
# reaches 0 or less.
#   * Every second day they drink water, which boosts their energy with 5% of their current energy
# and at the same time drops their water supplies by 30% of their current water.
#   # Every third day they eat, which reduces their food supplies (all food they have) be the
# following amount: {currentFood} / {countOfPeople} and at the same time raises their group's
# energy by 10%.
# The copping of wood, the drinking of water, and the eating happen in the order above. If they
# have enough energy to finish the quest, print the following message:
#       "You are ready for the quest. You will be left with - {energyLevel} energy!"
# If they run out of energy, print the following message and the food and water they were left
# with before they ran out of energy:
#       "You will run out of energy. You will be left with {food} food and {water} water."
# Input / Constraints
#   1st line: the days N of the adventure - an integer in the range[1...100]
#   2nd line: the number of players - an integer in the range[1 - 1000]
#   3rd line: the group's energy - a real number in the range[1 - 50000]
#   4th line: water per day for one person - a real number[0.00 - 1000.00]
#   5th line: food per day for one person - real number [0.00 - 1000.00]
#   On the next N lines - one for each of the days - the amount of energy loss - a real number
#   in the range [0.00 - 1000.00]
#   You will always have enough food and water
# The possible outputs are:
#   * "You are ready for the quest. You will be left with - {energyLevel} energy!"
#   * "You will run out of energy. You will be left with {food} food and {water} water."
# The final numbers should be formatted to the second digit after decimal separator
# Input	            Output
# 10                You are ready for the quest. You will be left with - 658.72 energy!
# 7
# 5035.5
# 11.3
# 7.2
# 942.3
# 500.57
# 520.68
# 540.87
# 505.99
# 630.3
# 784.20
# 321.21
# 456.8
# 330
# ---------------------------------------------------------------------------------------
# 12                You will run out of energy. You will be left with 229.17 food and 118.59 water.
# 6
# 4430
# 9.8
# 5.5
# 620.3
# 840.2
# 960.1
# 220
# 340
# 674
# 365
# 345.5
# 212
# 412.12
# 258
# 496
