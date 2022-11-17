text = list(input())
clean_list = []
previous_char = ""

for char in text:
    if char != previous_char:
        clean_list.append(char)
    previous_char = char

print("".join(clean_list))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a string from the console and replaces any sequence of the same letters
# with a single corresponding letter.
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# aaaaabbbbbcdddeeeedssaa	        abcdedsa
# --------------------------------------------
# qqqwerqwecccwd	                qwerqwecwd
