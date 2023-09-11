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

    

# ------------------------------------- Problem to resolve ------------------------------
#
# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's
# rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
#   * "potion" - You are healed with the number in the second part. But your health cannot exceed your
#       initial health (100). First print:
#                       * "You healed for {amount} hp."
#       After that, print your current health:
#                       *"Current health: {health} hp."
#   * "chest"
#       You've found some bitcoins, the number in the second part. Print:
#                       * "You found {amount} bitcoins."
#   * In any other case, you are facing a monster, which you will fight. The second part of the room
#       contains the attack of the monster. You should remove the monster's attack from your health.
#       If you are not dead (health <= 0), you've slain the monster, and print:
#                       * "You slayed {monster}."
#       If you've died, print
#                       * "You died! Killed by {monster}." and your quest is over.
#       Print the best room you've manage to reach:
#                       * "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
#                       * "You've made it!"
#                       * "Bitcoins: {bitcoins}"
#                       * "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar):"room1|room2|room3…".
# Output
# Print the corresponding messages described above.
# Input	                                                        Output
# rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000	You slayed rat.
#                                                               You slayed bat.
#                                                               You healed for 10 hp.
#                                                               Current health: 80 hp.
#                                                               You slayed rat.
#                                                               You found 100 bitcoins.
#                                                               You died! Killed by boss.
#                                                               Best room: 6
# ---------------------------------------------------------------------------------------
# cat 10|potion 30|orc 10|chest 10|snake 25|chest 110	        You slayed cat.
#                                                               You healed for 10 hp.
#                                                               Current health: 100 hp.
#                                                               You slayed orc.
#                                                               You found 10 bitcoins.
#                                                               You slayed snake.
#                                                               You found 110 bitcoins.
#                                                               You've made it!
#                                                               Bitcoins: 120
#                                                               Health: 65
