initial_health = 100
bitcoins = 0
current_health = initial_health

all_rooms = input().split("|")
room_count = 0
failed = False

for room in all_rooms:
    room_count += 1
    cmd = room.split(" ")
    command = cmd[0]
    value = int(cmd[1])
    if command == "potion":
        previous_health = current_health
        current_health += value
        if current_health >= 100:
            value = initial_health - previous_health
            current_health = 100
        print(f"You healed for {value} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        current_health -= value
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            failed = True
            break
if not failed:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {current_health}")
