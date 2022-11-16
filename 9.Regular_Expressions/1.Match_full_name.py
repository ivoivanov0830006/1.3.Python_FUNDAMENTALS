import re

text = input()
# pattern = r"\b[A-Z][a-z]+ +[A-Z][a-z]+\b"
pattern = "\\b[A-Z][a-z]+\s[A-Z][a-z]+\\b"

names = re.findall(pattern, text)
print(" ".join(names))


# ------------------------------------- Problem to resolve ------------------------------
#
# First, write a regular expression to match a valid full name, according to these conditions:
#   ⦁	A valid full name has the following characteristics:
#   ⦁	It consists of two words.
#   ⦁	Each word starts with a capital letter.
#   ⦁	After the first letter, it only contains lowercase letters.
#   ⦁	Each of the two words should be at least two letters long.
#   ⦁	A single space separates the two words.
# -------------------------------------- Example inputs ----------------------------------
# Input
# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett
# Output
# Peter Smith Lily Everett
