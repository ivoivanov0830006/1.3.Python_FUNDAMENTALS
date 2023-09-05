def calculator(operator):
    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        return int(number_1 / number_2)
    elif operator == "add":
        return number_1 + number_2
    elif operator == "subtract":
        return number_1 - number_2


operator = input()
number_1 = int(input())
number_2 = int(input())
print(calculator(operator))

# ------------------------------------- Another Solution -----------------------------

# def calculator(number_1, number_2, operation):
#     if operation == "multiply":
#         return number_1 * number_2
#     elif operation == "divide":
#         return int(number_1 - number_2)
#     elif operation == "add":
#         return number_1 + number_2
#     elif operation == "subtract":
#         return number_1 - number_2
#
#
# input_operator = input()
# first_number = int(input())
# second_number = int(input())
# print(calculator(first_number, second_number, input_operator))

# ------------------------------------- Problem to resolve ------------------------------
#
# Create a function that receives three parameters, calculates a result depending on the given
# operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", "subtract".
# Input	                Output
# subtract              1
# 5
# 4
# --------------------------------------
# divide                2
# 8
# 4
