password = input()
final_password = password

while True:
    command = input()
    if command == "Done":
        break
    action = command.split()[0]
    if action == "TakeOdd":
        current_password = ""
        for index in range(len(final_password)):
            if index % 2 != 0:
                current_password += final_password[index]
        final_password = current_password
        print(final_password)
    elif action == "Cut":
        start_index = int(command.split()[1])
        length = int(command.split()[2])
        end_index = start_index + length
        final_password = final_password[:start_index] + final_password[end_index:]
        print(final_password)
    elif action == "Substitute":
        substring = command.split()[1]
        substitute = command.split()[2]
        if substring in final_password:
            final_password = final_password.replace(substring, substitute)
            print(final_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {final_password}")
