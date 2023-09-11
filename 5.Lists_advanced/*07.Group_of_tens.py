numbers_list = list(map(int, input().split(", ")))

group = 10

while len(numbers_list) > 0:
    current_group = [num for num in numbers_list if num <= group]
    for number in current_group:
        if number in numbers_list:
            numbers_list.remove(number)
    print(f"Group of {group}'s: {current_group}")
    group += 10


# ------------------------------------- Another Solution -----------------------------
#
# args = input().split(", ")
# numbers_list = [int(x) for x in args]
#
# max_number = max(numbers_list) // 10
# if max(numbers_list) % 10 != 0:
#     max_number += 1
#
# total_groups = [[] for group in range(max_number)]
#
# for number in args:
#     if len(number) < 2:
#         group = 0
#     else:
#         if int(number) % 10 == 0:
#             group = int(number[0]) - 1
#         else:
#             group = int(number[0])
#     total_groups[group].append(int(number))
#
# count = 0
# for group in total_groups:
#     count += 10
#     print(f"Group of {count}'s: {group}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a sequence of args (a string containing integers separated by ", ") and prints the
# args sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
#       The args 2, 8, 4, and 10 fall into the group of 10's.
#       The args 13, 19, 14, and 15 fall into the group of 20's.
# Input                                 Output
# 8, 12, 38, 3, 17, 19, 25, 35, 50	    Group of 10's: [8, 3]
#                                       Group of 20's: [12, 17, 19]
#                                       Group of 30's: [25]
#                                       Group of 40's: [38, 35]
#                                       Group of 50's: [50]
# ----------------------------------------------------------------
# 1, 3, 3, 4, 34, 35, 25, 21, 33	    Group of 10's: [1, 3, 3, 4]
#                                       Group of 20's: []
#                                       Group of 30's: [25, 21]
#                                       Group of 40's: [34, 35, 33]
