numbers = list(map(int, input().split()))

total_left_sum = 0
total_right_sum = 0


finish_index = int(len(numbers) / 2)

for index in range(finish_index):
    if numbers[index] == 0:
        total_left_sum *= 0.8
    else:
        total_left_sum += numbers[index]

for index in range(len(numbers) - 1, finish_index, -1):
    if numbers[index] == 0:
        total_right_sum *= 0.8
    else:
        total_right_sum += numbers[index]

if total_right_sum >= total_left_sum:
    print(f"The winner is left with total time: {total_left_sum:.1f}")
else:
    print(f"The winner is right with total time: {total_right_sum:.1f}")

# total_right_sum = sum([args[idx] for idx in range(args[finish_index])])
