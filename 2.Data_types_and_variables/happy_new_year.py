year = int(input())
unique_year = False
current_year = 0

while not unique_year:
    current_year = str(year)
    set_year = set()
    for symbol in range(0, len(current_year)):
        set_year.add(str(current_year)[symbol])

    unique_year = len(set_year) == len(str(current_year))
    year += 1
print(current_year)


# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
# Input	        Output
# 8989	        9012
# 1001	        1023
