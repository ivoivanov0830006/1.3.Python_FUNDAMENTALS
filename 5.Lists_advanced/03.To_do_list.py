unsorted_list = []

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    current_importance = int(current_command[0])
    current_note = current_command[1]
    unsorted_list.append([current_importance, current_note])

final_list = []

sorted_list = sorted(unsorted_list)
for lst in sorted_list:
    char = lst.pop(1)
    final_list.append(char)
print(final_list)


# ------------------------------------- Another Solution -----------------------------
#
#
# tasks = []
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     split_command = command.split("-")
#     current_priority = int(split_command[0])
#     current_task = split_command[1]
#     tasks.append([current_priority, current_task])
#
# # -------------------------------------------------------------
# # sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
# sorted_tasks = []
# for task_data in sorted(tasks):
#     sorted_tasks.append(task_data[1])
#
# print(sorted_tasks)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
#   "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# 2-Walk the dog                    ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
# ---------------------------------------------------------------------------------------
# 3-C                               ['B', 'A', 'C', 'V']
# 2-A
# 1-B
# 6-V
# End

