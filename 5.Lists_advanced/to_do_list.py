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
