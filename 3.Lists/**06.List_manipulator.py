def exchange_func(my_number_list, index: int):
    for item in my_number_list[:index + 1]:
        my_number_list.append(item)
        my_number_list.remove(item)
    return my_number_list


def max_func(my_number_list, number_type: str):
    current_idx = 'No matches'
    max_number = 0
    if number_type == 'even':
        for index, number in enumerate(my_number_list):
            if number % 2 == 0:
                if number >= max_number:
                    max_number = number
                    current_idx = index
        return current_idx
    elif number_type == 'odd':
        for index, number in enumerate(my_number_list):
            if number % 2 != 0:
                if number >= max_number:
                    max_number = number
                    current_idx = index
        return current_idx


def min_func(my_number_list, number_type: str):
    current_idx = 'No matches'
    min_number = max(my_number_list)
    if number_type == 'even':
        for index, number in enumerate(my_number_list):
            if number % 2 == 0:
                if number <= min_number:
                    min_number = number
                    current_idx = index
        return current_idx
    elif number_type == 'odd':
        for index, number in enumerate(my_number_list):
            if number % 2 != 0:
                if number <= min_number:
                    min_number = number
                    current_idx = index
        return current_idx


def first_func(my_number_list, number_count: int, number_type: str):
    odd_list = []
    even_list = []
    for num in my_number_list:
        if num % 2 != 0:
            odd_list.append(num)
        elif num % 2 == 0:
            even_list.append(num)
    if number_type == "odd":
        return odd_list[0:number_count]
    elif number_type == "even":
        return even_list[0:number_count]


def last_func(my_number_list, number_count: int, number_type: str):
    odd_list = []
    even_list = []
    for num in my_number_list:
        if num % 2 != 0:
            odd_list.append(num)
        elif num % 2 == 0:
            even_list.append(num)
    if number_type == "odd":
        return odd_list[-number_count:]
    elif number_type == "even":
        return even_list[-number_count:]


input_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    current_command = command.split()
    current_action = current_command[0]
    if current_action == "exchange":
        current_index = int(current_command[1])
        if current_index >= len(input_list) or current_index < 0:
            print("Invalid index")
            continue
        input_list = exchange_func(input_list, current_index)
    elif current_action == "max":
        current_input = current_command[1]
        print(max_func(input_list, current_input))
    elif current_action == "min":
        current_input = current_command[1]
        print(min_func(input_list, current_input))
    elif current_action == "first":
        current_count = int(current_command[1])
        current_input = current_command[2]
        if current_count > len(input_list) or current_count < 0:
            print("Invalid count")
            continue
        print(first_func(input_list, current_count, current_input))
    elif current_action == "last":
        current_count = int(current_command[1])
        current_input = current_command[2]
        if current_count > len(input_list) or current_count < 0:
            print("Invalid count")
            continue
        print(last_func(input_list, current_count, current_input))

print(input_list)


# ------------------------------------- Problem to resolve ------------------------------
#
# The list may be manipulated by one of the following commands:
#   "exchange {index}" – splits the list after the given index and exchanges the places of the two sub-lists.
#           - E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
#           - If the index is outside the boundaries of the list, print "Invalid index"
#           - A negative index is considered invalid
#   "max even/odd"– returns the INDEX of the max even/odd element.
#           - E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
#   "min even/odd" – returns the INDEX of the min even/odd element.
#           - E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
#           - If there are two or more equal min/max elements, return the index of the rightmost one
#           - If a min/max even/odd element cannot be found, print "No matches"
#   "first {count} even/odd" – returns the first count even/odd elements.
#           - E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
#   "last {count} even/odd" – returns the last count even/odd elements.
#           -E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
#           - If the count is greater than the list length, print "Invalid count"
#           - If there are not enough elements to satisfy the count, print as many as you can.
#           - If there are zero even/odd elements, print an empty list "[]"
#   "end" - stop taking input and print the final state of the list
# Input
# The input data should be read from the console.
# On the first line, the initial list is received as a line of integers, separated by a single space.
# On the following lines, until the command "end" is received, you will receive the list manipulation commands.
# The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# The output should be printed on the console.
# On a separate line, print the output of the corresponding command.
# On the last line, print the final list in square brackets with its elements separated by a comma and a space.
# See the examples below to get a better understanding of your task.
# Constraints
# The number of input lines will be in the range [2 … 50].
# The list elements will be integers in the range [0 … 1000].
# The number of elements will be in the range [1 .. 50].
# The split index will be an integer in the range [-231 … 231 – 1].
# The first/last count will be an integer in the range [1 … 231 – 1].
# There will not be redundant whitespace anywhere in the input.
# Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 1 3 5 7 9                 2
# exchange 1                No matches
# max odd                   [5, 7]
# min even                  []
# first 2 odd               [3, 5, 7, 9, 1]
# last 2 even
# exchange 3
# end
# --------------------------------------------
# 1 10 100 1000             3
# max even                  Invalid count
# first 5 even              Invalid index
# exchange 10               0
# min odd                   2
# exchange 0                0
# max even                  [10, 100, 1000, 1]
# min even
# end
# --------------------------------------------
# 1 10 100 1000             [1]
# exchange 3                [1]
# first 2 odd               [1, 10, 100, 1000]
# last 4 odd
# end
