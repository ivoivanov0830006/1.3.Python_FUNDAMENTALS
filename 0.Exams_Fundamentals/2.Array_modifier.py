array = list(map(int, input().split()))
cmd = input()

while cmd != "end":
    command = cmd.split()
    action = command[0]
    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1] *= array[index_2]
    elif action == "decrease":
        array = [num - 1 for num in array]

    cmd = input()

print(*array, sep=", ")
