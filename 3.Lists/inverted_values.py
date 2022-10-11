numbers = input()
negative_numbers_list = []

numbers_list = list(numbers.split(" "))

for string in numbers_list:
    negative_number = -int(string)
    negative_numbers_list.append(negative_number)

print(negative_numbers_list)

# --------------------------- Problem to resolve -----------------------------
#
# Write a program that receives a single string containing positive and negative numbers
# separated by a single space. Print a list containing the opposite of each number.
# Input	                                Output
# 1 2 -3 -3 5	                        [-1, -2, 3, 3, -5]
# ------------------------------------------------------------
# -4 0 2 57 -101	                    [4, 0, -2, -57, 101]
