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

