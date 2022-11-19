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


# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" 
# command is given, you will be receiving strings with instructions for different operations that need to 
# be performed upon the concealed message to interpret it and reveal its true content. There are several 
# types of instructions, split by '|'
# "Move {number of letters}":
#       Moves the first n letters to the back of the string
# "Insert {index} {value}":
#       Inserts the given value before the given index in the string
# "ChangeAll {substring} {replacement}":
#       Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# On the first line, you will receive a string with a message.
# On the following lines, you will be receiving commands, split by '|' .
# Output
# After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# zzHe                              The decrypted message is: Hello
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode
# -------------------------------------------------------------------------
# owyouh                            The decrypted message is: howareyou?
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode
