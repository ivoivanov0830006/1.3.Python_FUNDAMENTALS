parking = {}

cars_count = int(input())

for cars in range(cars_count):
    current_input = input().split()
    command = current_input[0]

    if command == "register":
        username = current_input[1]
        license_plate = current_input[2]
        if username not in parking.keys():
            parking[username] = license_plate
            print(f"{username} registered {parking[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")

    elif command == "unregister":
        username = current_input[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]


for workers_name, cars_license_plate in parking.items():
    print(f"{workers_name} => {cars_license_plate}")

    
# ------------------------------------- Problem to resolve ------------------------------
#
# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online
# service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good
# thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister
# to leave.
# The program receives 2 types of commands:
#       "register {username} {license_plate_number}":
# The system only supports one car per user at the moment, so if a user tries to register another license
# plate using the same username, the system should print:
#       "ERROR: already registered with plate number {license_plate_number}"
# If the check above passes successfully, the user should be registered, so the system should print:
#       "{username} registered {license_plate_number} successfully"
#       "unregister {username}":
# If the user is not present in the database, the system should print:
#       "ERROR: user {username} not found"
# If the check above passes successfully, the system should print:
#       "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license
# plates in the format:
#       "{username} => {license_plate_number}"
# Input
# First line: n - number of commands - integer
# Next n lines: commands in one of the two possible formats:
# Register: "register {username} {license_plate_number}"
# Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# 5                                 John registered CS1234JS successfully
# register John CS1234JS            George registered JAVA123S successfully
# register George JAVA123S          Andy registered AB4142CD successfully
# register Andy AB4142CD            Jesica registered VR1223EE successfully
# register Jesica VR1223EE          Andy unregistered successfully
# unregister Andy	                John => CS1234JS
#                                   George => JAVA123S
#                                   Jesica => VR1223EE
# ----------------------------------------------------------------------------
# 4                                 Jony registered AA4132BB successfully
# register Jony AA4132BB            ERROR: already registered with plate number AA4132BB
# register Jony AA4132BB            Linda registered AA9999BB successfully
# register Linda AA9999BB           Jony unregistered successfully
# unregister Jony	                Linda => AA9999BB
# -----------------------------------------------------------------------------
# 6                                 Jacob registered MM1111XX successfully
# register Jacob MM1111XX           Anthony registered AB1111XX successfully
# register Anthony AB1111XX         Jacob unregistered successfully
# unregister Jacob                  Joshua registered DD1111XX successfully
# register Joshua DD1111XX          ERROR: user Lily not found
# unregister Lily                   Samantha registered AA9999BB successfully
# register Samantha AA9999BB        Anthony => AB1111XX
#                                   Joshua => DD1111XX
#                                   Samantha => AA9999BB
