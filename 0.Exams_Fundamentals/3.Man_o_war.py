def total_health(lst):
    result = sum(lst)
    return result


my_ship = list(map(int, input().split(">")))
enemy_ship = list(map(int, input().split(">")))
max_health = int(input())

need_repair_list = []

sunk_my_ship = False
sunk_enemy_ship = False

while True:
    command = input().split(" ")
    action = command[0]
    if action == "Retire":
        break

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(enemy_ship)):
            enemy_ship[index] -= damage
            if enemy_ship[index] <= 0:
                sunk_enemy_ship = True
                break

    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(my_ship)) and end_index in range(len(my_ship)):
            for idx in range(start_index, end_index + 1):
                my_ship[idx] -= damage
                if my_ship[idx] <= 0:
                    sunk_my_ship = True
                    break

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(my_ship)):
            my_ship[index] += health
            if my_ship[index] > max_health:
                my_ship[index] = max_health

    elif action == "Status":
        need_repair_list = [sect for sect in my_ship if sect < 0.2 * max_health]
        print(f"{len(need_repair_list)} sections need repair.")


if sunk_enemy_ship:
    print("You won! The enemy ship has sunken.")
elif sunk_my_ship:
    print("You lost! The pirate ship has sunken.")
else:
    print(f"Pirate ship status: {total_health(my_ship)}")
    print(f"Warship status: {total_health(enemy_ship)}")

    
# -------------------------------- Problem to resolve -----------------------------
#
# Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the
# first line, you will receive the status of the pirate ship, which is a string representing integer
# sections separated by ">". On the second line, you will receive the same type of status, but for
# the warship:
#       "{section1}>{section2}>{section3}… {section}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
# Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the
# warship sinks, print the following and stop the program:
#       "You won! The enemy ship has sunken."
# "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given
# damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip
# the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and
# stop the program:
#       "You lost! The pirate ship has sunken."
# "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
# Check if the index is valid and if not, skip the command. The health of the section cannot exceed
# the maximum health capacity.
# "Status" - prints the count of all sections of the pirate ship that need repair soon, which are
# all sections that are lower than 20% of the maximum health capacity. Print the following:
#       "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their
# individual sections, in the following format:
#       "Pirate ship status: {pirateShipSum}
#       Warship status: {warshipSum}"
# Input
# On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# On the 2nd line, you are going to receive the status of the warship
# On the 3rd line, you will receive the maximum health a section of a ship can reach.
# On the following lines, until "Retire", you will be receiving commands.
# Output
# Print the output in the format described above.
# Constraints
# The section numbers will be integers in the range [1….1000]
# The indexes will be integers [-200….200]
# The damage will be an integer in the range [1….1000]
# The health will be an integer in the range [1….1000]
# Input         	            Output
# 12>13>11>20>66                2 sections need repair.
# 12>22>33>44>55>32>18          Pirate ship status: 135
# 70                            Warship status: 205
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire
# ---------------------------------------------------------------------
# 2>3>4>5>2                     3 sections need repair.
# 6>7>8>9>10>11                 You lost! The pirate ship has sunken.
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 18
# Retire
