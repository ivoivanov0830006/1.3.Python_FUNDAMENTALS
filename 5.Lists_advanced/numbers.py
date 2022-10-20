sequence = list(map(int, input().split()))
new_list = [num for num in sequence if num > (sum(sequence) / len(sequence))]

if len(new_list) < 1:
    print("No")
new_list.sort(reverse=True)
print(*new_list[:5], sep=" ")


# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the
# average value in the sequence, sorted in descending order.
# Input
# Read from the console a single line holding space-separated integers.
# Output
# Print the above-described numbers on a single line, space-separated.
# If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# Print "No" if no numbers hold the above property.
# Constraints
# All input numbers are integers in the range [-1000000 … 1000000].
# The count of numbers is in the range [1…10 000].
# Examples
# Input	                                    Output
# 10 20 30 40 50	                        50 40
