sequence = input().split()
move_count = 0

while True:
    command = input()

    if len(sequence) == 0:
        print(f"You have won in {move_count} turns!")
        break

    if command == "end":
        print("Sorry you lose :(")
        print(f'{" ".join(sequence)}')
        break

    event = command.split()
    index_1 = int(event[0])
    index_2 = int(event[1])
    move_count += 1

    if index_1 < 0 or index_2 < 0 or index_1 == index_2 or index_1 >= len(sequence) or index_2 >= len(sequence):
        middle = int(len(sequence) / 2)
        sequence.insert(middle, f"-{move_count}a")
        sequence.insert(middle, f"-{move_count}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence[index_1] == sequence[index_2]:
        number = sequence[index_1]
        print(f"Congrats! You have found matching elements - {sequence[index_1]}!")
        sequence.remove(number)
        sequence.remove(number)

    else:
        print(f"Try again!")
    
    
# -------------------------------- Problem to resolve -----------------------------
#
# On the first line, you will receive a sequence of elements. Each element in the sequence will have
# a twin. Until the player receives "end" from the console, you will receive strings with two integers
# separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the
# sequence, you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# On the first line, you will receive a sequence of elements
# On the following lines, you will receive integers until the command "end"
# Output
# Every time the player hit two matching elements, you should remove them from the sequence and print
# on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# If the player hit all matching elements before he receives "end" from the console, you should print
# on the console the following message:
# "You have won in {number of moves until now} turns!"
# If the player receives "end" before he hits all matching elements, you should print on the console
# the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# All elements in the sequence will always have a matching element.
# Input 	                        Output
# 1 1 2 2 3 3 4 4 5 5               Congrats! You have found matching elements - 1!
# 1 0                               Invalid input! Adding additional elements to the board
# -1 0                              Congrats! You have found matching elements - 2!
# 1 0                               Congrats! You have found matching elements - 3!
# 1 0                               Congrats! You have found matching elements - -2a!
# 1 0                               Sorry you lose :(
# end	                            4 4 5 5
