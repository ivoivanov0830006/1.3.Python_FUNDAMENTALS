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
