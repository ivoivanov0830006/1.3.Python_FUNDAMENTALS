cells = input().split("#")

water = int(input())

high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)

total_effort = 0
total_fire = 0
extinguished_cells = []

for items in cells:
    current_cell = items.split(" = ")
    fire_type = current_cell[0]
    fire_power = int(current_cell[1])
    if water < fire_power:
        continue
    if (fire_type == "High" and fire_power in high or
            fire_type == "Medium" and fire_power in medium or
            fire_type == "Low" and fire_power in low):
        water -= fire_power
        total_effort += fire_power * 0.25
        total_fire += fire_power
        extinguished_cells.append(fire_power)
    if water <= 0:
        break

print("Cells:")
for number in extinguished_cells:
    print(f" - {number}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

# ----------------------------------------- Problem to resolve ----------------------------------
#
# Create a program that calculates the water needed to put out a "fire cell", based on the given information
# about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which
# represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires. There is a
# range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid,
# and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out
# fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value.
# In the end, you will have to print the total effort. Keep putting out cells until you run out of water.
# Skip it and try the next one if you do not have enough water to put out a given cell. In the end, print
# the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"
# Input / Constraints
# On the 1st line, you will receive the fires with their cells in the format described above –
# integer args in the range [1…500].
# On the 2nd line, you will receive the water – an integer number in the range [0….100000].
# Output
# Print the output as described above.
# Input	                                                                Output
# High = 89#Low = 28#Medium = 77#Low = 23                               Cells:
# 1250	                                                                 - 89
#                                                                        - 28
#                                                                        - 77
#                                                                        - 23
#                                                                       Effort: 54.25
#                                                                       Total Fire: 217
# ----------------------------------------------------------------------
# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77       Cells:
# 220	                                                                - 40
#                                                                       - 110
#                                                                       Effort: 37.50
#                                                                       Total Fire: 150
