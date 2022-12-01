import re

while True:
    text = input()
    if not text:
        break
    pattern = r"[0-9]+"
    numbers = re.finditer(pattern, text, flags=re.MULTILINE)

    for number in numbers:
        print(number.group(), end=" ")
     
    
# ------------------------------------- Another Solution -----------------------------
#
# import re
#
# pattern = r'\d+'
# line = input()
# while line:
#     matches = re.findall(pattern, line)
#     if matches:
#         print(" ".join(matches), end=" ")
#
#     line = input()


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives strings on different lines and extracts only the numbers. Print all
# extracted numbers on a single line, separated by a single space.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                        Output
# The300                                        300 3 22 45
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45
# ---------------------------------------------------------------------------
# 123a456                                       0	123 456 789 987 654 321 0
# 789b987
# 654c321
# ---------------------------------------------------------------------------
# Let's go11!!!11!                              11 11 1
# Okey!1!
