destinations = {}

while True:
    command = input()
    if command == "Sail":
        break

    city, population, gold = command.split("||")
    if city not in destinations:
        destinations[city] = {}
        destinations[city]["Population"] = int(population)
        destinations[city]["Gold"] = int(gold)
    else:
        destinations[city]["Population"] += int(population)
        destinations[city]["Gold"] += int(gold)

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("=>")
    action = current_command[0]
    if action == "Plunder":
        city, people, gold = current_command[1], current_command[2], current_command[3]
        if city in destinations.keys():
            destinations[city]["Population"] -= int(people)
            destinations[city]["Gold"] -= int(gold)
            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
            if destinations[city]["Population"] <= 0 or destinations[city]["Gold"] <= 0:
                print(f"{city} has been wiped off the map!")
                del destinations[city]
    elif action == "Prosper":
        city, gold = current_command[1], current_command[2]
        if city in destinations.keys():
            if int(gold) < 0:
                print("Gold added cannot be a negative number!")
                continue
            destinations[city]["Gold"] += int(gold)
            print(f"{gold} gold added to the city treasury. {city} now has {destinations[city]['Gold']} gold.")

if len(destinations) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    remaining_cities_count = len(destinations)
    print(f"Ahoy, Captain! There are {remaining_cities_count} wealthy settlements to go to:")
    for city in destinations:
        remaining_people = destinations[city]["Population"]
        remaining_gold = destinations[city]["Gold"]
        print(f"{city} -> Population: {remaining_people} citizens, Gold: {remaining_gold} kg")
