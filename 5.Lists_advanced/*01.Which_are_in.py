sequence_1 = input().split(", ")
sequence_2 = input().split(", ")
new_sequence = [string_1 for string_1 in sequence_1 if
                any(string_1 in string_2 for string_2 in sequence_2)]
print(new_sequence)


# ------------------------------------- Another Solution -----------------------------
#
# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = []
# for first_word in first_sequence:
#     for second_word in second_sequence:
#         if first_word in second_word:
#             substrings.append(first_word)
#             break
# print(substrings)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given two sequences of strings, separated by ", ". Print a new list containing only the
# strings from the first input line, which are substrings of any string in the second input line.
# Input	                                    Output
# arp, live, strong                         ['arp', 'live', 'strong']
# lively, alive, harp, sharp, armstrong
# -------------------------------------------------------------------------
# tarp, mice, bull                          []
# lively, alive, harp, sharp, armstrong

