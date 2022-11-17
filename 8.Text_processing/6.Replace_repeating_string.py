text = list(input())
clean_list = []
previous_char = ""

for char in text:
    if char != previous_char:
        clean_list.append(char)
    previous_char = char

print("".join(clean_list))
