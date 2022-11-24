concealed_message = input()
final_message = concealed_message

while True:
    command = input()
    if command == "Reveal":
        break
    current_command = command.split(":|:")
    action = current_command[0]

    if action == "InsertSpace":
        index = int(current_command[1])
        final_message = final_message[:index] + " " + final_message[index:]
        print(final_message)

    elif action == "Reverse":
        substring = current_command[1]
        if substring in final_message:
            final_message = final_message.replace(substring, "", 1)
            substring = substring[::-1]
            final_message = final_message + substring
            print(final_message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        final_message = final_message.replace(substring, replacement)
        print(final_message)

print(f"You have a new text message: {final_message}")
