some_text = input()
new_text = ""
strength = 0

for index in range(len(some_text)):
    if strength > 0 and some_text[index] != ">":
        strength -= 1
    elif some_text[index] == ">":
        new_text += some_text[index]
        strength += int(some_text[index + 1])
    else:
        new_text += some_text[index]

print(new_text)


# ------------------------------------- Another Solution -----------------------------
#
# explosion_list = input().split(">")
#
# new_list = [explosion_list[0]]
# previous_count = 0
#
# for explosion in explosion_list:
#     count = 0
#     if explosion[0].isdigit():
#         power = int(explosion[0]) + previous_count
#         new_explosion = explosion[power:]
#         new_list.append(new_explosion)
#         previous_count = 0
#         if power > len(explosion):
#             count += power - len(explosion)
#             previous_count = count
#
# print(">".join(new_list))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a string from the console that contains:
# ⦁	Explosions marked with '>'
# ⦁	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# ⦁	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another
# explosion mark ('>') while deleting characters, you should add the strength to your previous explosion.
# You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
# ⦁	You will always receive strength for the explosions
# ⦁	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# ⦁	The strength of the punches will be in the interval [0…9]
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# abv>1>1>2>2asdasd	                    abv>>>>dasd
# -----------------------------------------------------------
# pesho>2sis>1a>2akarate>4hexmaster	    pesho>is>a>karate>master

