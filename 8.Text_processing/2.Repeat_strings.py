words = input().split()
new_word = ""

for word in words:
    new_word += word * len(word)

print(new_word)


# ------------------------------------- Another Solution -----------------------------
#
# [print(word * len(word), end="") for word in input().split()]

# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a sequence of strings, separated by a single space.
# Each string should be repeated N times, where N is the length of the string.
# Print the final strings concatenated into one string.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# hi abc add	            hihiabcabcabcaddaddadd
# work	                    workworkworkwork
# ball	                    ballballballball
