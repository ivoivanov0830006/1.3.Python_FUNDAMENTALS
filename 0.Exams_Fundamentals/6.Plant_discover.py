number_plants = int(input())
exhibition = {}

for _ in range(number_plants):
    plant_name, description = input().split("<->")
    if plant_name not in exhibition:
        rating = [0]
        exhibition[plant_name] = []
        exhibition[plant_name].append(description)
        exhibition[plant_name].append(rating)
    else:
        exhibition[plant_name].append(description)

while True:
    command = input()
    if command == "Exhibition":
        break

    current_command = command.split(": ")
    action = current_command[0]
    if action == "Rate":
        plant, current_rating = current_command[1].split(" - ")
        if plant in exhibition:
            exhibition[plant][1].insert(0, int(current_rating))
        else:
            print("error")

    elif action == "Update":
        plant, new_rarity = current_command[1].split(" - ")
        if plant in exhibition:
            exhibition[plant][0] = int(new_rarity)
        else:
            print("error")

    elif action == "Reset":
        plant = current_command[1]
        if plant in exhibition:
            exhibition[plant][1] = [0]
        else:
            print("error")


print("Plants for the exhibition:")
for plant, description in exhibition.items():
    rarity = description[0]
    rating = sum(description[1])
    if len(description[1]) > 1:
        rating = sum(description[1]) / (len(description[1]) - 1)
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")


# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line, you will receive a number n. On the next n lines, you will be given some information 
# about the plants that you have discovered in the format: 
#   * "{plant}<->{rarity}". 
# Store that information because you will need it later. If you receive a plant more than once, update its 
# rarity. After that, until you receive the command "Exhibition", you will be given some of these commands:
#   * "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
#   * "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
#   * "Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following 
# format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                        Output
# 3                                             Plants for the exhibition:
# Arnoldii<->4                                  - Arnoldii; Rarity: 4; Rating: 0.00
# Woodii<->7                                    - Woodii; Rarity: 5; Rating: 7.50
# Welwitschia<->2                               - Welwitschia; Rarity: 2; Rating: 7.00
# Rate: Woodii - 10         
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition	
# ----------------------------------------------------------------------------------------
# 2                                             Plants for the exhibition:
# Candelabra<->10                               - Candelabra; Rarity: 10; Rating: 6.00
# Oahu<->10                                     - Oahu; Rarity: 10; Rating: 7.00
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition	
