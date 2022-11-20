input_text = input()

final_text = input_text

while True:
    command = input()
    if command == "Generate":
        break

    current_command = command.split(">>>")
    action = current_command[0]

    if action == "Contains":
        sub_string = current_command[1]
        if sub_string in final_text:
            print(f"{final_text} contains {sub_string}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        case = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if case == "Upper":
            final_text = final_text[:start_index] + (final_text[start_index:end_index]).upper() + final_text[end_index:]
            print(final_text)
        elif case == "Lower":
            final_text = final_text[:start_index] + (final_text[start_index:end_index]).lower() + final_text[end_index:]
            print(final_text)
    elif action == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        final_text = final_text[:start_index] + final_text[end_index:]
        print(final_text)


print(f"Your activation key is: {final_text}")
