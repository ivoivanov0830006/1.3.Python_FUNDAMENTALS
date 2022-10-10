input_list = input().split()

round_list = []

for string in input_list:
    number = float(string)
    round_list.append(round(number))
print(round_list)


# ------------------------------------- Another Solution -----------------------------
#
# result = list(map(lambda x: round(float(x)), input().split("")))
# print(result)
#
#
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().
# Input	                            Output
# 1.0 2.5 3.0 4.5	                [1, 2, 3, 4]
# 2.56 1.9 -3.4 8.1	                [3, 2, -3, 8]
