numbers = int(input())

for number in range(1, numbers + 1):
    result = False
    total_sum = 0
    for digit in str(number):
        total_sum += int(digit)
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        result = True
    print(f"{number} -> {result}")


# --------------------------- Another solution ----------------------------
#
# numbers = int(input())
#
# for number in range(1, numbers + 1):
#     result = False
#     total_sum = 0
#     digits = number
#     while digits > 0:
#         total_sum += digits % 10
#         digits = int(digits / 10)
#     if total_sum == 5 or total_sum == 7 or total_sum == 11:
#         result = True
#     print(f"{number} -> {result}")

# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False). A number is special
# when the sum of its digits is 5, 7, or 11.
# Input	            Output
# 15	            1 -> False
#                   2 -> False
#                   3 -> False
#                   4 -> False
#                   5 -> True
#                   6 -> False
#                   7 -> True
#                   8 -> False
#                   9 -> False
#                   10 -> False
#                   11 -> False
#                   12 -> False
#                   13 -> False
#                   14 -> True
#                   15 -> False
# -----------------------------------------
# 6	                1 -> False
#                   2 -> False
#                   3 -> False
#                   4 -> False
#                   5 -> True
#                   6 -> False
