targets = list(map(int, input().split()))

while True:
    command = input().split(" ")
    action = command[0]
    if action == "End":
        break
    index = int(command[1])

    if action == "Shoot":
        power = int(command[2])
        if index in range(len(targets)):
            target = targets[index] - power
            if target > 0:
                targets[index] = target
            else:
                targets.pop(index)
    elif action == "Add":
        value = int(command[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(command[2])
        left_part = index - radius
        right_part = index + radius
        if left_part in range(len(targets)) and right_part in range(len(targets)):
            targets = targets[0:left_part] + targets[right_part + 1::]
        else:
            print("Strike missed!")

print(f"{'|'.join(list(map(str, targets)))}")
