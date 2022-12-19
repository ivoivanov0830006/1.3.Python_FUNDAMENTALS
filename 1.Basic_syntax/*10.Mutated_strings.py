word_1 = input()
word_2 = input()
new_word = ""
last_word = ""
n = 1

for _ in range(len(word_1)):
    new_word += word_2[:n] + word_1[n:]
    n += 1
    if new_word != word_1 and new_word != last_word:
        print(new_word)
        last_word = new_word
        new_word = ""
    else:
        new_word = ""
        continue

        
# ----------------------------------- Another solution ---------------------------------
# word_1 = input()
# word_2 = input()
#
# for char in range(len(word_1)):
#     if word_1[char] != word_2[char]:
#         word_1 = word_1[:char] + word_1[char:char + 1].replace(word_1[char], word_2[char], 1) + word_1[char + 1:]
#         print(word_1)


# ------------------------------------ Another solution ---------------------------------
# word_1 = input()
# word_2 = input()
# new_list = list(word_1)
#
# for char in range(len(word_1)):
#     if new_list[char] != word_2[char]:
#         new_list[char] = word_2[char]
#         print("".join(new_list))


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
# -------------------------------------- Example inputs ----------------------------------
# Input	                Output
# bubble gu             tubble gum
# turtle hum            turble gum
#                       turtle gum
#                       turtle hum
# ---------------------------------------------
# Kitty                 Ditty
# Doggy	                Dotty
#                       Dogty
#                       Doggy
