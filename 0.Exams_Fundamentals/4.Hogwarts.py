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
