input_text = input().split()
string_1 = input_text[0]
string_2 = input_text[1]
total = 0

if len(string_1) > len(string_2):
    for index in range(len(string_2)):
        total += ord(string_1[index]) * ord(string_2[index])

    for index in range(len(string_2), len(string_1)):
        total += ord(string_1[index])


elif len(string_1) < len(string_2):
    for index in range(len(string_1)):
        total += ord(string_1[index]) * ord(string_2[index])

    for index in range(len(string_1), len(string_2)):
        total += ord(string_2[index])


else:
    for index in range(len(string_1)):
        total += ord(string_1[index]) * ord(string_2[index])

print(total)
