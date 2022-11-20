initial_stops = input()
final_string = initial_stops

command = input()
while command != "Travel":
    current_command = command.split(":")
    action = current_command[0]
    if action == "Add Stop":
        index = int(current_command[1])
        new_stop = current_command[2]
        if 0 <= index <= len(final_string) - 1:
            final_string = final_string[:index] + new_stop + final_string[index:]
    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index >= 0 and end_index <= len(final_string) - 1:
            final_string = final_string[:start_index] + final_string[end_index + 1:]
    elif action == "Switch":
        old_location = current_command[1]
        new_location = current_command[2]
        if old_location in final_string:
            final_string = final_string.replace(old_location, new_location)

    print(final_string)
    command = input()

print(f"Ready for world tour! Planned stops: {final_string}")
