secret_message = input().split()
for words in secret_message:
    number = int("".join(i for i in words if i.isdigit()))
    word = "".join(i for i in words if i.isalpha())
    first_letter = chr(number)
    word_list = list(word)
    word_list.insert(0, first_letter)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    print("".join(word_list), end=" ")


# ------------------------------------- Problem to resolve ------------------------------
#
# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)
# Input	                    Output
# 72olle 103doo 100ya	    Hello good day
# ------------------------------------------
# 82yade 115te 103o	        Ready set go
