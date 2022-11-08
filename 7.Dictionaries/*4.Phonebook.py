phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone

for check in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

        
# ------------------------------------- Another Solution -----------------------------
#
# phonebook = {}
#
# while True:
#     command = input().split("-")
#     if command[0].isdigit():
#         break
#     name, number = command[0], command[1]
#     phonebook[name] = number
#
# people_count = int(command[0])
#
# for _ in range(people_count):
#     person = input()
#     if person in phonebook.keys():
#         print(f"{person} -> {phonebook[person]}")
#     else:
#         print(f"Contact {person} does not exist.")


# ------------------------------------- Problem to resolve ------------------------------
# Write a program that receives info from the console about people and their phone numbers.
#
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name
# that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a
# search of contact by name and print its details in the format: "{name} -> {number}". In case the
# contact isn't found, print: "Contact {name} does not exist."
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# Adam-0888080808                   Contact Mery does not exist.
# 2                                 Adam -> 0888080808
# Mery
# Adam
# ------------------------------------------------------------------
# Adam-+359888001122                Silvester -> 02/987665544
# Ralf-666                          Contact silvester does not exist.
# George-5559393                    Contact Rolf does not exist.
# Silvester-02/987665544            Ralf -> 666
# 4
# Silvester
# silvester
# Rolf
# Ralf
