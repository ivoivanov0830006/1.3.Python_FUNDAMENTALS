import re

input_text = input()
pattern = r"(?P<sep>[#|@])(?P<word_one>[a-zA-Z]{3,})(?P=sep){2}(?P<word_two>[a-zA-Z]{3,})(?P=sep)"
matches = re.findall(pattern, input_text)

mirrored_words = []
valid_pairs_count = 0

for match in matches:
    valid_pairs_count += 1
    word_one = match[1]
    word_two = match[2]

    if word_one == word_two[::-1]:
        mirrored_words.append(word_one)
        mirrored_words.append(word_two)
        # mirrored_words.append(f"{word_one} <=> {word_two}")
final_dict = []

if valid_pairs_count == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{valid_pairs_count} word pairs found!")
    if len(mirrored_words) != 0:
        for index in range(0, len(mirrored_words), 2):
            first_word = mirrored_words[index]
            second_word = mirrored_words[index + 1]
            final_dict.append(first_word + " <=> " + second_word)
        print("The mirror words are:")
        print(", ".join(final_dict))
    else:
        print("No mirror words!")
 

# ------------------------------------- Another Solution -----------------------------
#
# import re
# 
# input_text = input()
# pattern = r"(?P<sep>[#|@])(?P<word_one>[a-zA-Z]{3,})(?P=sep){2}(?P<word_two>[a-zA-Z]{3,})(?P=sep)"
# matches = re.findall(pattern, input_text)
# 
# mirrored_words = []
# valid_pairs_count = 0
# 
# for match in matches:
#     valid_pairs_count += 1
#     word_one = match[1]
#     word_two = match[2]
# 
#     if word_one == word_two[::-1]:
#         mirrored_words.append(f"{word_one} <=> {word_two}")
# 
# 
# if valid_pairs_count == 0:
#     print("No word pairs found!")
#     print("No mirror words!")
# else:
#     print(f"{valid_pairs_count} word pairs found!")
#     if not mirrored_words:
#         print("No mirror words!")
#     else:
#         print("The mirror words are:")
#         print(", ".join(mirrored_words))


# ------------------------------------- Problem to resolve -----------------------------------------
#
# On the first line of the input, you will be given a text string. To win the competition, you have to find
# all hidden word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
#   * Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
#   * At least 3 characters long each (without the surrounding symbols)
#   * Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they
# are a match, and you have to store them somewhere. Examples of mirror words: #Part##traP# @leveL@@Level@ #sAw##wAs#
# If you don`t find any valid pairs, print:
#       "No word pairs found!"
# If you find valid pairs print their count:
#       "{valid pairs count} word pairs found!"
# If there are no mirror words, print:
#       "No mirror words!"
# If there are mirror words print:
#       "The mirror words are:
#       {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# -------------------------------------- Example inputs ----------------------------------
# Input
# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
# Output
# 5 word pairs found!
# The mirror words are:
# Part <=> traP, leveL <=> Level, sAw <=> wAs
# --------------------------------------------
# Input
# #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@
# Output
# 2 word pairs found!
# No mirror words!
# --------------------------------------------
# Input
# #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#
# Output	Comments
# No word pairs found!
# No mirror words!
