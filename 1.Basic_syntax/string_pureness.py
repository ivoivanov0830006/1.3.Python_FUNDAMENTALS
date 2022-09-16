for string in range(int(input())):
    is_pure = True
    text = input()
    for char in range(len(text)):
        if text[char] == "," or text[char] == "." or text[char] == "_":
            is_pure = False
            break
        else:
            continue
    if is_pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
        
# --------------------------- Another solution ----------------------------
#
# for string in range(int(input())):
#     text = input()
#     if "," in text or "." in text or "_" in text:
#         print(f"{text} is pure.")
#     else:
#         print(f"{text} is not pure!"

# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure, meaning that they do NOT consist
# of any of the characters: comma ",", period ".", or underscore "_":
#   - If a string is pure, print "{string} is pure."
#   - Otherwise, print "{string} is not pure!"
# Input                     # Output
# 2
# pure string               pure string is pure.
# not_pure_string	        not_pure_string is not pure!      
# ----------------------------------------------------------
# 3
# SoftUni                   SoftUni is pure.
# 12345                     12345 is pure.
# string.pureness	        string.pureness is not pure!
