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



# --------------------------- Problem to resolve -----------------------------
# As a young traveler, you gather items and craft new items.
# Input / Constraints
# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
#   * "Collect - {item}" - you should add the given item to your inventory. If the item already exists,
# you should skip this line.
#   * "Drop - {item}" - you should remove the item from your inventory if it exists.
#   * "Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the
# new item after the old one. Otherwise, ignore the command.
#   * "Renew – {item}" – if the given item exists, you should change its position and put it last in your
# inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", ".
# Input	                            Output
# Iron, Wood, Sword                 Iron, Sword, Gold
# Collect - Gold
# Drop - Wood
# Craft!
# ---------------------------------------------------------------------------
# Iron, Sword                       Sword, Bow, Iron
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
