text = input()

for index in range(len(text)):
    if text[index] == ":":
        next_char = text[index + 1]
        # if text[index] == ":" and index != len(text) - 1:
        print(f":{next_char}")

        
# ------------------------------------- Problem to resolve ------------------------------
#
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
# -------------------------------------- Example inputs ----------------------------------
# Input                         	                        Output
# There are so many emoticons nowadays :P.                  :P
# I have many ideas :O what input to place here :)	        :O
#                                                           :)
