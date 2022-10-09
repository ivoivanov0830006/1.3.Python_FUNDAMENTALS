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
