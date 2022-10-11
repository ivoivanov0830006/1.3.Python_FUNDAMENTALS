factor = int(input())
count = int(input())
start = factor
end = factor * count

new_list = []

for number in range(start, end + 1):
    if number % factor == 0:
        new_list.append(number)
print(new_list)

# --------------------------- Another solution ----------------------------
#
# factor = int(input())
# count = int(input())
# new_list = []
# number = 0
#
# for _ in range(1, count + 1):
#     number += factor
#     new_list.append(int(number))
#
# print(new_list)
#
# --------------------------- Another solution ----------------------------
#
# factor = int(input())
# count = int(input())
#
# new_list = []
#
# for multiplier in range(1, count + 1):
#     new_list.append(factor * multiplier)
# print(new_list)
#
# --------------------------- Problem to resolve -----------------------------
#
# Write a program that receives two numbers (factor and count). It should create a list with a length
# of the given count that contains only integer numbers, which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order, starting from
# the value of the factor.
# Input	                    Output
# 2                         [2, 4, 6, 8, 10]
# 5
# --------------------------------------------------
# 1                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10
