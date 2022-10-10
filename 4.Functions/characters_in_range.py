def ascii_range(character1, character2):
    ascii_list = []
    start = ord(character1)
    final = ord(character2)

    for char in range(start + 1, final):
        letter = chr(char)
        ascii_list.append(letter)
    result = (" ".join(ascii_list))
    return result


char_1 = input()
char_2 = input()
total_result = ascii_range(char_1, char_2)
print(total_result)
