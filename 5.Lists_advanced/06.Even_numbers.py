numbers = list(map(int, input().split(", ")))
indexes = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(indexes)


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a single string with args separated by comma and space ", ".
# Print the indices of all even args.
# Input	                            Output
# 3, 2, 1, 5, 8	                    [1, 4]
# -------------------------------------------
# 2, 4, 6, 9, 10	                [0, 1, 2, 4]

