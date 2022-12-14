spell = input()

while True:
    command = input()
    if command == "Abracadabra":
        break
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif action == "Illusion":
        index = int(current_command[1])
        letter = current_command[2]
        if index in range(len(spell)):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif action == "Divination":
        first_substring = current_command[1]
        second_substring = current_command[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif action == "Alteration":
        substring = current_command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")

  
# ------------------------------------- Problem to resolve ------------------------------
#
# First you will receive a spell that needs to be deciphered. Next, you will be receiving commands
# split by a single space until you get the "Abracadabra" command. There are 5 possible commands:
#     * "Abjuration"
#         Replace all letters with upper case and print the result
#     * "Necromancy"
#         Replace all letters with lower case and print the result
#     * "Illusion {index} {letter}"
#         Replace the letter at the index with the given one and print "Done!"
#         If the index is invalid print: "The spell was too weak."
#     * "Divination"
#         Replace the first substring (all matches) with the second print the result.
#         If the substring does not exist, skip the command.
#     * "Alteration"
#         Remove the substring from the string and prin the result.
#         If the substring does not exist, skip the command.
#     If the input command is not in the list, print "The spell did not work!".
# Input/Constraints
#     * On the first line, you are going to receive the string.
#     * On the next lines, until you receive "Abracadabra", you will be receiving commands.
#     * All command are case-sensitive
# Output
#     * Print the output in the format described above
# -------------------------------------- Example inputs ----------------------------------
# Input                         Output
# A7ci0                         Done!
# Illusion 1 c                  Done!
# Illusion 4 o                  ACCIO
# Abjuration
# Abracadabra
# ---------------------------------------------------------------
# TR1GG3R                       tr1gg3r
# Necromancy                    The spell was too weak.
# Illusion 8 m                  The spell was too weak.
# Illusion 9 n
# Abracadabra
# ---------------------------------------------------------------
# SwordMaster                   The spell did not work!
# Target Target Target          SWORDMASTER
# Abjuration                    swordmaster
# Necromancy                    sword
# Alteration master
# Abracadabra
