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
