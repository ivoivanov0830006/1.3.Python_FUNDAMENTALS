def loading(number):
    percentage = ""
    for _ in range(1, int(number / 10) + 1):
        percentage += "%"
    for _ in range(1, 11 - (int(number / 10))):
        percentage += "."
    if number != 100:
        print(f"{number}% [{percentage}]\nStill loading...")
    else:
        print(f"{number}% Complete!\n[{percentage}]")


input_percentage = int(input())

loading(input_percentage)


# ------------------------------------- Another Solution -----------------------------
#
# def loading(number):
#     if number == 100:
#         return f"{number}% Complete!\n[{'%' * (number // 10)}]"
#     return f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."
#
#
# input_percentage = int(input())
#
# print(loading(input_percentage))
#
# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without
# remainder (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending
# on the number you have received in the input. Print the result on the console. For more clarification,
# see the examples below.
# Input	                        Output
# 30	                        30% [%%%.......]
#                               Still loading...
# -------------------------------------------------
# 50	                        50% [%%%%%.....]
#                               Still loading...
# -------------------------------------------------
# 100	                        100% Complete!
#                               [%%%%%%%%%%]
