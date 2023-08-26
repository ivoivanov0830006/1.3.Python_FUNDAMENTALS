sequence_numbers = list(map(int, input().split()))
input_message = input()
print(sequence_numbers)

new_word = []

for index in range(len(sequence_numbers)):
    number = [int(i) for i in str(sequence_numbers[index])]
    current_index = sum(number)
    if current_index > len(input_message):
        pass
    else:
        char = input_message[current_index]
        new_word.append(char)
        input_message.remove(char)
