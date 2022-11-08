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

