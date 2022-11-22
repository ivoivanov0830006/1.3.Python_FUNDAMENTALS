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

        
# ------------------------------------- Problem to resolve -----------------------------------------
#
# Until the "Sail" command is given, you will be receiving:
# You and your crew have targeted cities, with their population and gold, separated by "||".
# If you receive a city that has already been received, you have to increase the population and gold with
# the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
#   * "Plunder=>{town}=>{people}=>{gold}"
# You have successfully attacked and plundered the town, killing the given number of people and stealing the
# respective amount of gold.
# For every town you attack print this message:
#       - "{town} plundered! {gold} gold stolen, {people} citizens killed."
# If any of those two values (population or gold) reaches zero, the town is disbanded.
# You need to remove it from your collection of targeted cities and print the following message:
#       - "{town} has been wiped off the map!"
# There will be no case of receiving more people or gold than there is in the city.
#   * "Prosper=>{town}=>{gold}"
# There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print:
#       - "Gold added cannot be a negative number!" and ignore the command.
# If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print
# the following message:
#       - "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# After receiving the "End" command, if there are any existing settlements on your list of targets, you need
# to print all of them, in the following format:
#       - "Ahoy, Captain! There are {count} wealthy settlements to go to:
#          {town1} -> Population: {people} citizens, Gold: {gold} kg
#          {town2} -> Population: {people} citizens, Gold: {gold} kg
#           …
#          {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# If there are no settlements left to plunder, print:
#       * "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
# The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed
# the respective limits. The town names in the events will always be valid towns that should be on your list.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# Tortuga||345000||1250                 Tortuga plundered! 380 gold stolen, 75000 citizens killed.
# Santo Domingo||240000||630            180 gold added to the city treasury. Santo Domingo now has 810 gold.
# Havana||410000||1100                  Ahoy, Captain! There are 3 wealthy settlements to go to:
# Sail                                  Tortuga -> Population: 270000 citizens, Gold: 870 kg
# Plunder=>Tortuga=>75000=>380          Santo Domingo -> Population: 240000 citizens, Gold: 810 kg
# Prosper=>Santo Domingo=>180           Havana -> Population: 410000 citizens, Gold: 1100 kg
# End
# -----------------------------------------------------------------------------------------
# Nassau||95000||1000                   Gold added cannot be a negative number!
# San Juan||930000||1250                Nassau plundered! 750 gold stolen, 94000 citizens killed.
# Campeche||270000||690                 Nassau plundered! 150 gold stolen, 1000 citizens killed.
# Port Royal||320000||1000              Nassau has been wiped off the map!
# Port Royal||100000||2000              Campeche plundered! 690 gold stolen, 150000 citizens killed.
# Sail                                  Campeche has been wiped off the map!
# Prosper=>Port Royal=>-200             Ahoy, Captain! There are 2 wealthy settlements to go to:
# Plunder=>Nassau=>94000=>750           San Juan -> Population: 930000 citizens, Gold: 1250 kg
# Plunder=>Nassau=>1000=>150            Port Royal -> Population: 420000 citizens, Gold: 3000 kg
# Plunder=>Campeche=>150000=>690
# End
