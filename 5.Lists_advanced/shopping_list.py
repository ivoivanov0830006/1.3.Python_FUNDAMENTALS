initial_list = input().split("!")

while True:
    cmd = input()
    if cmd == "Go Shopping!":
        break
    command = cmd.split(" ")
    action = command[0]
    if action == "Urgent":
        item = command[1]
        if item in initial_list:
            continue
        else:
            initial_list.insert(0, item)
    elif action == "Unnecessary":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            initial_list = list(map(lambda x: x.replace(old_item, new_item), initial_list))
    elif action == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# "Urgent {item}" - add the item at the start of the list.  If the item already exists, skip
# this command.
# "Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
# Otherwise, skip this command.
# "Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name
# with the new one. Otherwise, skip this command.
# "Rearrange {item}" - if the grocery exists in the list, remove it from its current position
# and add it at the end of the list. Otherwise, skip this command.
# Constraints
# There won't be any duplicate items in the initial list
# Output
# Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"
# Input                 	            Output
# Tomatoes!Potatoes!Bread               Tomatoes, Potatoes, Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!
# --------------------------------------------------------------
# Milk!Pepper!Salt!Water!Banana         Milk, Onion, Salt, Water, Banana
# Urgent Salt
# Unnecessary Grapes
# Correct Pepper Onion
# Rearrange Grapes
# Correct Tomatoes Potatoes
# Go Shopping!
