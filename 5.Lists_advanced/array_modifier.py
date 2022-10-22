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


# ------------------------------------- Problem to resolve ------------------------------
#
# You are given an array with integers. Write a program to modify the elements after receiving the following
# commands:
# "swap {index1} {index2}" takes two elements and swap their places.
# "multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
# Save the product at the 1st index.
# "decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command "end". The commands are as follow:
#       * "swap {index1} {index2}"
#       * "multiply {index1} {index2}"
#       * "decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by
# a comma and a single space ", ".
# Constraints
# Elements of the array will be integer numbers in the range [-231...231]
# Count of the array elements will be in the range [2...100]
# Indexes will be always in the range of the array
# Input	                            Output
# 23 -2 321 87 42 90 -123           86, 7382, 2369942, -124, 41, 89, -3
# swap 1 3
# swap 3 6
# swap 1 0
# multiply 1 2
# multiply 2 1
# decrease
# end
# -------------------------------------------------------------------------
# 1 2 3 4                           1, 11, 3, 0
# swap 0 1
# swap 1 2
# swap 2 3
# multiply 1 2
# decrease
# end
