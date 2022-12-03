initial_loot = input().split("|")
total_sum = 0

no_more_items = False

while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    elif action == "Loot":
        items = command[1:]
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif action == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            current_item = initial_loot.pop(index)
            initial_loot.append(current_item)

    elif action == "Steal":
        count = int(command[1])
        stolen_items = []
        if count >= len(initial_loot):
            print(", ".join(initial_loot))
            no_more_items = True
            break
        else:
            for items in range(count):
                item = initial_loot.pop()
                stolen_items.insert(0, item)
            print(", ".join(stolen_items))

if no_more_items:
    print("Failed treasure hunt.")
else:
    for item in initial_loot:
        total_sum += len(item)
    average_gain = total_sum / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
