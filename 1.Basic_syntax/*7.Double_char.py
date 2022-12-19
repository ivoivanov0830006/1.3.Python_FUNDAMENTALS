command = input()

while command != "End":
    is_break = False
    new_word = ""
    for char in range(len(command)):
        if command == "SoftUni":
            is_break = True
            break
        else:
            new_word += command[char] + command[char]
    if is_break:
        print(new_word, end="")    # because after break there is EMPTY line in the results ! ! ! ! ! 
    else:
        print(new_word)
    command = input()
