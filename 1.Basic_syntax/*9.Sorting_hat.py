command = input()
wrong = False

while command != "Welcome!":
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif command == "Voldemort":
        wrong = True
        break
    else:
        print(f"{command} goes to Hufflepuff.")
    command = input()
if not wrong:
    print("Welcome to Hogwarts.")
else:
    print("You must not speak of that name!")


# ------------------------------------- Problem to resolve ------------------------------
#
# Help out the sorting hat to sort the new students in the houses of Hogwarts.
# You will be receiving names until the command "Welcome!". The length of each name
# determines in which house the student is going:
#   - If the name is less than 5 chars, the student is going into Gryffindor
#           Print "{name} goes to Gryffindor."
#   - If the name is exactly 5 chars, the student is going into Slytherin
#           Print "{name} goes to Slytherin."
#   - If the name is exactly 6 chars, the student is going into Ravenclaw
#           Print "{name} goes to Ravenclaw."
#   - If the name is more than 6 chars, the student is going into Hufflepuff
#           Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!"
# and end the program. No more sorting for today!
#   - If all students are sorted successfully:
#           Print "Welcome to Hogwarts."
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# Harry                             Harry goes to Slytherin.
# Ron                               Ron goes to Gryffindor.
# Ginny                             Ginny goes to Slytherin.
# Draco                             Draco goes to Slytherin.
# Welcome!                          Welcome to Hogwarts.
# -------------------------------------------------------------------
# Luna                              Luna goes to Gryffindor.
# Hermione                          Hermione goes to Hufflepuff.
# Neville                           Neville goes to Hufflepuff.
# Voldemort	                        You must not speak of that name!
