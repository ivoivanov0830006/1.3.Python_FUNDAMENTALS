# text = "".join(input().split())
text = input().replace(" ", "")

letters = {}

for char in text:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")
    

# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# text	                t -> 2
#                       e -> 1
#                       x -> 1
# ------------------------------
# text text text        t -> 6
# 	                    e -> 3
#                       x -> 3
