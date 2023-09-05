def palindrome(num_list):
    for number in num_list:
        num_string = str(number)
        size = len(num_string)
        reversed_num = num_string[size::-1]
        if reversed_num == number:
            print("True")
        else:
            print("False")


numbers_list = list(input().split(", "))
palindrome(numbers_list)

# ------------------------------------- Problem to resolve ------------------------------
#
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
# Input	                        Output
# 123, 323, 421, 121	        False
#                               True
#                               False
#                               True
# 32, 2, 232, 1010	            False
#                               True
#                               True
#                               False

