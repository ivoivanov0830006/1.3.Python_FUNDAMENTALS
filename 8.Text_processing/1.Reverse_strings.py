while True:
    input_word = input()
    if input_word == "end":
        break
    print(f"{input_word} = {input_word[::-1]}")
