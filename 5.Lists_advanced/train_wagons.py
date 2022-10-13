number_wagons = int(input())
train = [0] * number_wagons

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split(" ")
    process = current_command[0]

    if process == "add":
        people = int(current_command[1])
        train[-1] += people
    elif process == "insert":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] += people
    elif process == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] -= people

print(train)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a number representing the number of wagons a train has. Create a list (train) with
# the given length containing only zeros. Until you receive the command "End", you will receive some of
# the following commands:
#   · "add {people}" – you should add the number of people in the last wagon
#   · "insert {index} {people}" - you should add the number of people at the given wagon
#   · "leave {index} {people}" - you should remove the number of people from the wagon. There will be
# no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.
# Input                             Output
# 3                                 [10, 0, 20]
# add 20
# insert 0 15
# leave 0 5
# End
