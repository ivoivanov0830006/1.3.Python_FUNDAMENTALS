dictionary = {}
max_words = int(input())

while max_words > 0:
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    if synonym not in dictionary[word]:
        dictionary[word].append(synonym)
        max_words -= 1

for key, value in dictionary.items():
    value_list = ", ".join(value)
    print(f"{key} - {value_list}")
