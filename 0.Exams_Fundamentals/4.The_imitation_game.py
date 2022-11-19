def move_func(text, number_of_letters):
    result = text[number_of_letters:] + text[:number_of_letters]
    return result


def insert_func(text, index, value):
    left_part = text[:index]
    right_part = text[index:]
    result = left_part + value + right_part
    return result


def replace_func(text, substring, replacement):
    result = text.replace(substring, replacement)
    return result


initial_text = input()

while True:
    command = input()
    if command == "Decode":
        break
    current_command = command.split("|")
    action = current_command[0]

    if action == "Move":
        given_number = int(current_command[1])
        initial_text = move_func(initial_text, given_number)

    elif action == "Insert":
        given_index = int(current_command[1])
        given_string = current_command[2]
        initial_text = insert_func(initial_text, given_index, given_string)

    elif action == "ChangeAll":
        given_substring = current_command[1]
        given_replacement = current_command[2]
        initial_text = replace_func(initial_text, given_substring, given_replacement)


print(f"The decrypted message is: {initial_text}")
