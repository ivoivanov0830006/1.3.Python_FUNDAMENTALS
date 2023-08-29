input_number = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(input_number):
    num = int(input())
    if num < 0:
        negative.append(num)
    if num >= 0:
        positive.append(num)
    if num % 2 == 0 or num == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)

command_line = input()
if command_line == "even":
    print(even)
elif command_line == "odd":
    print(odd)
elif command_line == "negative":
    print(negative)
elif command_line == "positive":
    print(positive)
