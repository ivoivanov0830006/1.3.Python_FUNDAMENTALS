def repeat_string(current_string, num):
    return current_string * num


string = input()
number = int(input())
print(repeat_string(string, number))

# ------------------------------------- Another Solution -----------------------------

# string = input()
# number = int(input())
# result = lambda str, num: str * num
# print(result(string, number))
