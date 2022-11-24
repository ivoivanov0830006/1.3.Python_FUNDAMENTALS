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


# ------------------------------------- Problem to resolve -----------------------------------------
#
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal"
# command is given, you will receive strings with instructions for different operations that need to be
# performed upon the concealed message to interpret it and reveal its actual content. There are several types
# of instructions, split by ":|:"
#    * "InsertSpace:|:{index}":
#       Inserts a single space at the given index. The given index will always be valid.
#    * "Reverse:|:{substring}":
#       If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#       If not, print "error". This operation should replace only the first occurrence of the given substring
#       if there are two or more occurrences.
#    * "ChangeAll:|:{substring}:|:{replacement}":
#       Changes all occurrences of the given substring with the replacement text.
# After the "Reveal" command is received, print this message:
#       "You have a new text message: {message}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# heVVodar!gniV                         hellodar!gnil
# ChangeAll:|:V:|:l                     hellodarling!
# Reverse:|:!gnil                       hello darling!
# InsertSpace:|:5                       You have a new text message: hello darling!
# Reveal
# ---------------------------------------------------------------------------------
# Hiware?uiy                            Howare?uoy
# ChangeAll:|:i:|:o                     Howareyou?
# Reverse:|:?uoy                        error
# Reverse:|:jd                          How areyou?
# InsertSpace:|:3                       How are you?
# InsertSpace:|:7                       You have a new text message: How are you?
# Reveal
#
