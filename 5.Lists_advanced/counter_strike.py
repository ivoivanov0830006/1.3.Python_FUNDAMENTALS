energy = int(input())
command = input()
wins = 0

while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        wins += 1
        if wins % 3 == 0:
            energy += wins
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        energy -= distance
        break
    command = input()
if energy >= 0:
    print(f"Won battles: {wins}. Energy left: {energy}")
