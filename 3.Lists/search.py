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
