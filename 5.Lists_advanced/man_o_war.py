sequence = input().split()
move_count = 0

while True:
    command = input()

    if len(sequence) == 0:
        print(f"You have won in {move_count} turns!")
        break

    if command == "end":
        print("Sorry you lose :(")
        print(f'{" ".join(sequence)}')
        break

    event = command.split()
    index_1 = int(event[0])
    index_2 = int(event[1])
    move_count += 1

    if index_1 < 0 or index_2 < 0 or index_1 == index_2 or index_1 >= len(sequence) or index_2 >= len(sequence):
        middle = int(len(sequence) / 2)
        sequence.insert(middle, f"-{move_count}a")
        sequence.insert(middle, f"-{move_count}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence[index_1] == sequence[index_2]:
        number = sequence[index_1]
        print(f"Congrats! You have found matching elements - {sequence[index_1]}!")
        sequence.remove(number)
        sequence.remove(number)

    else:
        print(f"Try again!")
