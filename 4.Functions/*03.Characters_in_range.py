def ascii_range(character1, character2):
    ascii_list = []
    start = ord(character1)
    final = ord(character2)

    for char in range(start + 1, final):
        letter = chr(char)
        ascii_list.append(letter)
    result = (" ".join(ascii_list))
    return result


char_1 = input()
char_2 = input()
total_result = ascii_range(char_1, char_2)
print(total_result)


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a function that receives two characters and returns a single string with all the characters in
# between them (according to the ASCII code), separated by a single space. Print the result on the console.
# Input	                        Output
# a                             b c
# d
# ------------------------------------------------------------------------------------------
# #                             $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
# :
# --------------------------------------------------------------------------------------------
# #                             $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
# C
