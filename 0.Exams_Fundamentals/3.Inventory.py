journal = input().split(", ")

cmd = input()

while cmd != "Craft!":
    command = cmd.split(" - ")
    action = command[0]
    if action == "Collect":
        item = command[1]
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        item = command[1]
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    elif action == "Renew":
        item = command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
    cmd = input()
print(", ".join(journal))
