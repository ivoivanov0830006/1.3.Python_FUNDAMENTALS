def aliquot_sum(input_number):
    total_sum = 0
    for divisor in range(1, input_number):
        if input_number % divisor == 0:
            total_sum += divisor
    if total_sum == input_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

aliquot_sum(number)


# ------------------------------------- Problem to resolve ------------------------------
#
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
#   - "We have a perfect number!" - if the number is perfect.
#   - "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
# Input	                Output 	                            Comments
# 6	                    We have a perfect number!	        1 + 2 + 3
# 28	                We have a perfect number!	        1 + 2 + 4 + 7 + 14
# 1236498	            It's not so perfect.

