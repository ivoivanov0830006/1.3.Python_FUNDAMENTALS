def min_num(my_numbers_list):
    min_number = min(my_numbers_list)
    return min_number


def max_num(my_numbers_list):
    max_number = max(my_numbers_list)
    return max_number


def sum_all_num(my_numbers_list):
    result = sum(my_numbers_list)
    return result


numbers_list = list(map(int, input().split(" ")))

minimum_number = min_num(numbers_list)
maximum_number = max_num(numbers_list)
total_sum = sum_all_num(numbers_list)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {total_sum}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
#   - On the first line: "The minimum number is {minimum number}"
#   - On the second line: "The maximum number is {maximum number}"
#   - On the third line: "The sum number is: {sum of all numbers}"
# Input	                    Output
# 2 4 6	                    The minimum number is 2
#                           The maximum number is 6
#                           The sum number is: 12
# -----------------------------------------------------
# 12 52 11 53 2 8 45	    The minimum number is 2
#                           The maximum number is 53
#                           The sum number is: 183
