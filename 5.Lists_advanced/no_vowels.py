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
#
