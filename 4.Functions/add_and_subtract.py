def sum_numbers(a, b):
    result = a + b
    return result


def subtract(sum_num, c):
    result = sum_num - c
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

total = subtract((sum_numbers(num_1, num_2)), num_3)
print(total)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive three integer numbers.
# Write functions named:
# sum_numbers() that returns the sum of the first two integers
# subtract() that returns the difference between the returned result of the first function and the third
# integer. Wrap the two functions in a function named add_and_subtract() which will receive the three
# numbers as parameters. Print the result of the subtract() function on the console.
# Input	                            Output
# 23                                19
# 6
# 10
# -------------------------------------------------
# 1                                 -12
# 17
# 30
# -------------------------------------------------
# 42                                0
# 58
# 100
