def factorial(number):
    for num in range(1, number):
        number *= num
    return number


def end_result(factorial_1, factorial_2):
    return f"{(factorial_1 / factorial_2):.2f}"


number_1 = int(input())
number_2 = int(input())

print(end_result(factorial(number_1), factorial(number_2)))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
# Input	                        Output
# 5                             60.00
# 2
# ---------------------------------------
# 6                             360.00
# 2
