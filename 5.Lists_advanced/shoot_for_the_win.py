sequence = list(map(int, input().split()))
count = 0

while True:
    command = input()
    if command == "End":
        break
    index_shot = int(command)
    if index_shot >= len(sequence):
        continue

    current_value = sequence[index_shot]
    sequence[index_shot] = -1
    for index in range(len(sequence)):
        if sequence[index] == -1:
            continue

        if sequence[index] > current_value:
            sequence[index] -= current_value
        elif sequence[index] <= current_value:
            sequence[index] += current_value
    count += 1

print(f"Shot targets: {count} -> {' '.join(list(map(str, sequence)))}")
