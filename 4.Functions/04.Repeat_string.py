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

# ------------------------------------- Problem to resolve ------------------------------
#
# Write a function that receives a string and a counter n. The function should return a new string –
# the result of repeating the old string n times. Print the result of the function. Try using lambda.
# Input	                            Output
# abc                               abcabcabc
# 3
# ------------------------------------------------
# String                            StringString
# 2
