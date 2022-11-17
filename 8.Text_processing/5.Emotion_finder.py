text = input()

for index in range(len(text)):
    if text[index] == ":":
        next_char = text[index + 1]
        # if text[index] == ":" and index != len(text) - 1:
        print(f":{next_char}")
