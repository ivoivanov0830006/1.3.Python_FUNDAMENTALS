input_text = input().split()
string_1 = input_text[0]
string_2 = input_text[1]
total = 0

if len(string_1) > len(string_2):
    for index in range(len(string_2)):
        total += ord(string_1[index]) * ord(string_2[index])

    for index in range(len(string_2), len(string_1)):
        total += ord(string_1[index])


elif len(string_1) < len(string_2):
    for index in range(len(string_1)):
        total += ord(string_1[index]) * ord(string_2[index])

    for index in range(len(string_1), len(string_2)):
        total += ord(string_2[index])


else:
    for index in range(len(string_1)):
        total += ord(string_1[index]) * ord(string_2[index])

print(total)


# ------------------------------------- Problem to resolve ------------------------------
#
# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0]
# and add the result to the total sum, then continue with the next two characters. If one of the strings
# is longer than the other, add the remaining character codes to the total sum without multiplication.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# George Peter	            52114
# --------------------------------
# 123 522	                7647
# --------------------------------
# a aaaa	                9700
