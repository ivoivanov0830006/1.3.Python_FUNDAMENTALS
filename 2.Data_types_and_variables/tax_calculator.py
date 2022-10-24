car_list = input().split(">>")

total_tax = 0

for car in car_list:
    command = car.split()
    type_car = command[0]
    years = int(command[1])
    distance = int(command[2])

    if type_car == "family":
        initial_tax = 50
        initial_tax -= 5 * years
        multiplier = distance // 3000
        if distance >= 3000:
            initial_tax += 12 * multiplier

    elif type_car == "heavyDuty":
        initial_tax = 80
        initial_tax -= 8 * years
        multiplier = distance // 9000
        if distance >= 9000:
            initial_tax += 14 * multiplier

    elif type_car == "sports":
        initial_tax = 100
        initial_tax -= 9 * years
        multiplier = distance // 2000
        if distance >= 2000:
            initial_tax += 18 * multiplier
    else:
        print("Invalid car type.")
        continue
    print(f"A {type_car} car will pay {initial_tax:.2f} euros in taxes.")
    total_tax += initial_tax

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")


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
