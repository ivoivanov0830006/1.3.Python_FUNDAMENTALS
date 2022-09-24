year = int(input())
unique_year = False
current_year = year

while not unique_year:
    year += 1
    current_year = str(year)
    set_year = set()
    for symbol in range(0, len(current_year)):
        set_year.add(current_year[symbol])

    unique_year = len(set_year) == len(str(current_year))

print(current_year)

# --------------------------- Another solution ----------------------------
#
# from itertools import permutations
# number = tuple(map(int, input()))
# mypermutation = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
#
# for digits in list(mypermutation):
#     if digits > number:
#         result = "".join(str(x) for x in digits)
#         print(result)
#         break

# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
# Input	        Output
# 8989	        9012
# 1001	        1023
