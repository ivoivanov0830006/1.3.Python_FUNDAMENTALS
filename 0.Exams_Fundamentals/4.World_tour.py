def add_stop_func(current_data):
    global final_string
    index = int(current_data[1])
    new_stop = current_data[2]
    if 0 <= index <= len(final_string) - 1:
        final_string = final_string[:index] + new_stop + final_string[index:]
        return final_string


def remove_stop_func(current_data):
    global final_string
    start_index = int(current_data[1])
    end_index = int(current_data[2])
    if start_index >= 0 and end_index <= len(final_string) - 1:
        final_string = final_string[:start_index] + final_string[end_index + 1:]
        return final_string
    return final_string


def switch_func(current_data):
    global final_string
    old_location = current_data[1]
    new_location = current_data[2]
    if old_location in final_string:
        final_string = final_string.replace(old_location, new_location)
        return final_string


initial_stops = input()
final_string = initial_stops

while True:
    command = input()
    if command == "Travel":
        break
    current_command = command.split(":")
    action = current_command[0]
    if action == "Add Stop":
        print(add_stop_func(current_command))
    elif action == "Remove Stop":
        print(remove_stop_func(current_command))
    elif action == "Switch":
        print(switch_func(current_command))

print(f"Ready for world tour! Planned stops: {final_string}")


# ------------------------------------- Another Solution -----------------------------
#
# initial_stops = input()
# final_string = initial_stops
#
# command = input()
# while command != "Travel":
#     current_command = command.split(":")
#     action = current_command[0]
#     if action == "Add Stop":
#         index = int(current_command[1])
#         new_stop = current_command[2]
#         if 0 <= index <= len(final_string) - 1:
#             final_string = final_string[:index] + new_stop + final_string[index:]
#     elif action == "Remove Stop":
#         start_index = int(current_command[1])
#         end_index = int(current_command[2])
#         if start_index >= 0 and end_index <= len(final_string) - 1:
#             final_string = final_string[:start_index] + final_string[end_index + 1:]
#     elif action == "Switch":
#         old_location = current_command[1]
#         new_location = current_command[2]
#         if old_location in final_string:
#             final_string = final_string.replace(old_location, new_location)
#
#     print(final_string)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {final_string}")


# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line, you will be given a string containing all of your stops. Until you receive the
# command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# "Add Stop:{index}:{string}":
#       Insert the given string at that index only if the index is valid
# "Remove Stop:{start_index}:{end_index}":
#       Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# "Switch:{old_string}:{new_string}":
#       If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# Hawai::Cyprys-Greece                  Hawai::RomeCyprys-Greece
# Add Stop:7:Rome                       Hawai::Rome-Greece
# Remove Stop:11:16                     Bulgaria::Rome-Greece
# Switch:Hawai:Bulgaria                 Ready for world tour! Planned stops: Bulgaria::Rome-Greece
# Travel
# --------------------------------------------------------------------------------------
# Albania:Bulgaria:Cyprus:Deuchland     AlbNigeriaania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria                    AlbNaania:Bulgaria:Cyprus:Deuchland
# Remove Stop:4:8                       AlbNaania:Bulgaria:Cyprus:Deuchland
# Switch:Albania: Azərbaycan            Ready for world tour! Planned stops: AlbNaania:Bulgaria:Cyprus:Deuchland
# Travel
