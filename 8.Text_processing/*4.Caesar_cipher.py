text = input()
new_text = ""

for char in text:
    new_text += chr(ord(char) + 3)

print(new_text)


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing
# each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# Programming is cool!	        Surjudpplqj#lv#frro$
# ----------------------------------------------------
# One year has 365 days.	    Rqh#|hdu#kdv#698#gd|v1
