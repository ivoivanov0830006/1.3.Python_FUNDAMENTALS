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
