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


# ------------------------------------- Problem to resolve ------------------------------
#
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for
# different operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# "Contains>>>{substring}":
#       If the raw activation key contains the given substring, prints: "{raw activation key} contains
#       {substring}". Otherwise, prints: "Substring not found!"
# "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
#       Changes the substring between the given indices (the end index is exclusive) to upper or lower case
#       and then prints the activation key. All given indexes will be valid.
# "Slice>>>{startIndex}>>>{endIndex}":
#       Deletes the characters between the start and end indices (the end index is exclusive) and prints the
#       activation key. Both indices will be valid.
# Input
# The first line of the input will be a string consisting of letters and numbers only.
# After the first line, until the "Generate" command is given, you will be receiving strings.
# Output
# After the "Generate" command is received, print:
#       * "Your activation key is: {activation key}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                    Output
# abcdefghijklmnopqrstuvwxyz                abghijklmnopqrstuvwxyz
# Slice>>>2>>>6                             abgHIJKLMNOPQRstuvwxyz
# Flip>>>Upper>>>3>>>14                     abgHIjkLMNOPQRstuvwxyz
# Flip>>>Lower>>>5>>>7                      Substring not found!
# Contains>>>def                            Substring not found!
# Contains>>>deF                            Your activation key is: abgHIjkLMNOPQRstuvwxyz
# Generate
# -----------------------------------------------------------------------------------------
# 134softsf5ftuni2020rockz42                134sf5ftuni2020rockz42
# Slice>>>3>>>7                             Substring not found!
# Contains>>>-rock                          Substring not found!
# Contains>>>-uni-                          Substring not found!
# Contains>>>-rocks                         134SF5FTuni2020rockz42
# Flip>>>Upper>>>2>>>8                      134SF5ftuni2020rockz42
# Flip>>>Lower>>>5>>>11                     Your activation key is: 134SF5ftuni2020rockz42
# Generate

