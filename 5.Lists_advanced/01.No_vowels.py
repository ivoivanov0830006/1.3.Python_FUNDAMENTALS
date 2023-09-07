text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [letter for letter in text if letter.lower() not in vowels]
print("".join(result))


# ------------------------------------- Another Solution -----------------------------
#
# text = input()
# vowels = ['a', 'o', 'u', 'e', 'i']
# result = ""
# for letter in text:
#     if letter.lower() not in vowels:
#         result += letter
#
# print(result)


# ------------------------------------- Problem to resolve ------------------------------
#
# Using comprehension, write a program that receives a text and removes all its vowels,
# case insensitive. Print the new text string after removing the vowels. The vowels that should be
# considered are 'a', 'o', 'u', 'e', 'i'.
# -------------------------------------- Example inputs ----------------------------------
# Input                 Output
# Python                Pythn
# -----------------------------------
# ILovePython           LvPythn
