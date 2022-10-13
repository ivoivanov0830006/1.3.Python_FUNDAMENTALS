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
