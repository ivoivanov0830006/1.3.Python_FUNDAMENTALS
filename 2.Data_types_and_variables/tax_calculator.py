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
# Every day they chop wood an lose certain amount of energy. For each of the days you are going
# to receive the amount of energy lost from chopping wood. The program should end if the energy
# reaches 0 or less.
