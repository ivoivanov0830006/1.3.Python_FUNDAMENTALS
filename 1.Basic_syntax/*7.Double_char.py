command = input()

while command != "End":
    is_break = False
    new_word = ""
    for char in range(len(command)):
        if command == "SoftUni":
            is_break = True
            break
        else:
            new_word += command[char] + command[char]
    if is_break:
        print(new_word, end="")    # because after break there is EMPTY line in the results ! ! ! ! ! 
    else:
        print(new_word)
    command = input()

    
# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given strings until you receive the command "End". For each string given,
# you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# Hello World           HHeelllloo  WWoorrlldd
# Repeat                RReeppeeaatt
# End
# ----------------------------------------------------------
# 1234!                 11223344!!
# SoftUni               ssooffttuunnii
# softuni
# End
