sequence = list(map(int, input().split()))
count = 0

while True:
    command = input()
    if command == "End":
        break
    index_shot = int(command)

    # continue if received invalid index
    if index_shot >= len(sequence):
        continue

    current_value = sequence[index_shot]
    sequence[index_shot] = -1
    for index in range(len(sequence)):

        # continue if target already shot
        if sequence[index] == -1:
            continue

        if sequence[index] > current_value:
            sequence[index] -= current_value
        elif sequence[index] <= current_value:
            sequence[index] += current_value
    count += 1

print(f"Shot targets: {count} -> {' '.join(list(map(str, sequence)))}")




# ------------------------------------- Another Solution -----------------------------
#
# def reduce_values(target_sequence, index_shot):
#     current_value = target_sequence[index_shot]
#     target_sequence[index_shot] = -1
#     for index in range(len(sequence)):
#         if target_sequence[index] == -1:
#             continue
#
#         if target_sequence[index] > current_value:
#             target_sequence[index] -= current_value
#         elif target_sequence[index] <= current_value:
#             target_sequence[index] += current_value
#     return sequence
#
#
# def shoot_for_the_win_func(target_sequence):
#     count = 0
#     while True:
#         command = input()
#         if command == "End":
#             break
#
#         index_shot = int(command)
#         if index_shot >= len(target_sequence):
#             continue
#         if 0 <= index_shot < len(target_sequence) and target_sequence[index_shot] != -1:
#             count += 1
#             reduce_values(target_sequence, index_shot)
#
#     print(f"Shot targets: {count} -> {' '.join(list(map(str, sequence)))}")
#
#
# sequence = list(map(int, input().split()))
# shoot_for_the_win_func(sequence)


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that helps you keep track of your shot targets. You will receive a sequence
# with integers, separated by a single space, representing targets and their value. Afterward,
# you will be receiving indices until the "End" command is given, and you need to print the
# targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that,
# you also need to:
#   * Reduce all the other targets, which have greater values than your current target, with its
#   value.
#   * Increase all the other targets, which have less than or equal value to the shot target,
#   with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or
# reduce a target, which is considered shot.
# When you receive the "End" command, print the targets in their current state and the count of
# shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
# On the first line of input, you will receive a sequence of integers, separated by a single
# space – the targets sequence.
# On the following lines, until the "End" command, you be receiving integers each on a single
# line – the index of the target to be shot.
# Output
# The format of the output is described above in the problem description.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 24 50 36 70               Shot targets 3 -> -1 -1 130 -1
# 0
# 4
# 3
# 1
# End
# ----------------------------------------------------------------
# 5                         Shot targets: 4 -> -1 120 -1 66 -1 -1
# 2
# 4
# 0
# End
