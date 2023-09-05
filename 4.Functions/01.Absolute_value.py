numbers = list(map(float, input().split(" ")))
result = [abs(num) for num in numbers]
print(result)

# ------------------------------------- Another Solution -----------------------------
#
# numbers = input().split()
# abs_list = []
#
# for string in numbers:
#     number = float(string)
#     abs_list.append(abs(number))
# print(abs_list)

# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a sequence of numbers, separated by a single space, and prints
# their absolute value as a list. Use abs().
# Input	                        Output
# 1 2.5 -3 -4.5	                [1.0, 2.5, 3.0, 4.5]
# -0 1 10 -6.66	                [0.0, 1.0, 10.0, 6.66]
