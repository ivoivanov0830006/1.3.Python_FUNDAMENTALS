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


# ------------------------------------- Problem to resolve -----------------------------------------
#
# Write a password reset program that performs a series of commands upon a predefined string. First, you 
# will receive a string, and afterward, until the command "Done" is given, you will be receiving strings 
# with commands split by a single space. The commands will be the following:
#   * "TakeOdd"
#  Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
#   * "Cut {index} {length}"
# Gets the substring with the given length starting from the given index from the password and removes its 
# first occurrence, then prints the password on the console.
# The given index and the length will always be valid.
#   * "Substitute {substring} {substitute}"
# If the raw password contains the given substring, replaces all of its occurrences with the substitute 
# text given and prints the result.
# If it doesn't, prints "Nothing to replace!".
# After the "Done" command is received, print:
#       "Your password is: {password}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                            Output
# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr        icecream::hot::summer
# TakeOdd                                           icecream::hot::mer
# Cut 15 3                                          icecream-hot-mer
# Substitute :: -                                   Nothing to replace!
# Substitute | ^                                    Your password is: icecream-hot-mer
# Done	
# --------------------------------------------------------------------
# up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy          programming!is!funny
# TakeOdd                                           programming!is!fun
# Cut 18 2                                          programming***is***fun
# Substitute ! ***                                  Nothing to replace!            
# Substitute ? .!.                                  Your password is: programming***is***fun
# Done	
