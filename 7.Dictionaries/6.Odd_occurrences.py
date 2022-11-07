sequence = input().split()
words_lowercase = []

words = {}

for word in sequence:
    words_lowercase.append(word.lower())

for key in words_lowercase:
    if key not in words.keys():
        words[key] = 0
    words[key] += 1

for key, occurrences in words.items():
    if occurrences % 2 != 0:
        print(f"{key}", end=" ")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that prints all elements from a given sequence of words that occur an odd number of
# times (case-insensitive) in it.
# ⦁	Words are given on a single line, space-separated.
# ⦁	Print the result elements in lowercase, in their order of appearance.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# Java C# PHP PHP JAVA C java	        java c# c
# -------------------------------------------------
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi	    5 hi
# -------------------------------------------------
# a a A SQL xx a xx a A a XX c	        a sql xx c
