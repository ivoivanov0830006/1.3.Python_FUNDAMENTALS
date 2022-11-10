while True:
    input_word = input()
    if input_word == "end":
        break
    print(f"{input_word} = {input_word[::-1]}")

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a single string. On the first line, print all the digits found in the
# string, on the second – all the letters, and on the third – all the other characters. There will always
# be at least one digit, one letter, and one other character.
# -------------------------------------- Example inputs ----------------------------------
# Input	Output
# Agd#53Dfg^&4F53	53453
# AgdDfgF
# #^&
