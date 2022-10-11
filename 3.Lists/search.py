input_number = int(input())
search_string = input()
default_list = []
fixed_list = []

for _ in range(1, input_number + 1):
    added_strings = input()
    default_list.append(added_strings)
    fixed_list.append(added_strings)
    added_strings_list = list(added_strings.split(" "))
    if search_string not in added_strings_list:
        fixed_list.remove(added_strings)


print(default_list)
print(fixed_list)

# --------------------------- Another solution ----------------------------
#
# total_strings = int(input())
# key_word = input()
# new_list = []
# filtered_list = []
#
# for _ in range(total_strings):
#     current_string = input()
#     new_list.append(current_string)
# print(new_list)
# for num in range(len(new_list) - 1, -1, -1):
#     word = new_list[num]
#     if key_word not in word:
#         new_list.remove(word)
# print(new_list)
#
# --------------------------- Problem to resolve -----------------------------
#
# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and
# print them. After that, you should filter out only the strings that include the given word
# and print that list too.
# Input	                            Output
# 3                                 ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
# SoftUni                           ["I study at SoftUni", "I learn Python at SoftUni"]
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
# ------------------------------------------------------------------------------------------------------
# 4                                 ["I love tomatoes", "I can eat tomatoes forever",
# tomatoes                          "I don't like apples", "Yesterday I ate two tomatoes"]
# I love tomatoes                   ["I love tomatoes", "I can eat tomatoes forever",
# I can eat tomatoes forever         "Yesterday I ate two tomatoes"]
# I don't like apples
# Yesterday I ate two tomatoes
