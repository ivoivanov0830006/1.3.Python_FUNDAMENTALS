import re

number_inputs = int(input())

pattern = r"^(?P<sep>%|\$)(?P<tag>[A-Z][a-z]{2,})(?P=sep):\s\[(?P<one>\d+)\]\|\[(?P<two>\d+)\]\|\[(?P<three>\d+)\]\|$"
# pattern = r"^(?P<sep>%|\$)([A-Z][a-z]{3,})(?P=sep):\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
for _ in range(number_inputs):
    input_text = input()
    match = re.search(pattern, input_text)
    if match:
        print(f"{match[2]}: {chr(int(match[3]))}{chr(int(match[4]))}{chr(int(match[5]))}")
    else:
        print("Valid message not found!")

        
# ------------------------------------- Problem to resolve ------------------------------
#
# Create a program that checks if inputs have a valid message and decrypt it. On the first line, you
# will receive a number that indicates how many inputs you will receive on the following lines.
# A message is valid when:
#     * There is nothing else before and after it.On
#     * It starts with tag, which is surrounded by either "$" ot "%" (but not both at the same time).
#       The tag itself has to be minimum 3 characters long, start with an uppercase letter, followed
#       only by lowercase letters:
#     * There is a colon and a single white space after the tag
#     * There are 3 groups consisting of numbers between "[" and "]", followed by pipe "|"
# Example for a valid message:
#     "$Request$: [73]|[115]|[32]|"
# You must check if the message is valid and if it is - decrypt it. If it in not - print the following:
#     "Valid message not found!"
# Decrypting message means taking all numbers and turn them into ASCII symbols. After successful decrypt,
# print it in following format:
#     "{tag}: {decryptedMessage}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                            Output
# 4                                                 Request: Isi
# $Request$: [73]|[115]|[105]|                      Valid message not found!
# %Taggy$: [73]|[73]|[73]|                          Taggy: val
# %Taggy%: [118]|[97]|[108]|                        Valid message not found!
# $Request$: [73]|[115]|[105]|[32]|[75]|
# --------------------------------------------------------------------------
# 3                                                 Valid message not found!
# This shouldnt be valid%Taggy%: [118]|[97]|[108]|  Valid message not found!
# $tAGged$: [97][97][97]|                           Valid message not found!
# $Request$: [73]|[115]|[105]|true
