number_chars = int(input())
total_sum = 0

for _ in range(number_chars):
    char = input()
    letter = ord(char)
    total_sum += letter
print(f"The sum equals: {total_sum}")


# --------------------------- Problem to resolve ----------------------------


# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines. On the following N lines –
# you will receive a letter per line. Print the total sum in the following format:
#   - "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].
# Input	                    Output
# 5                         The sum equals: 399
# A
# b
# C
# d
# E
# ----------------------------------------------------
# 12                        The sum equals: 1263
# S
# o
# f
# t
# U
# n
# i
# R
# u
# l
# z
# z
