import re

number_inputs = int(input())

pattern = r"^(?P<sep>%|\$)(?P<tag>[A-Z][a-z]{2,})(?P=sep):\s\[(?P<one>\d+)\]\|\[(?P<two>\d+)\]\|\[(?P<three>\d+)\]\|$"
# pattern = r"^(?P<sep>%|\$)([A-Z][a-z]{3,})(?P=sep):\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
for _ in range(number_inputs):
    input_text = input()
    match = re.search(pattern, input_text)
    if match:
        print(f"{match[2]}: {chr(int(match[3]))}{chr(int(match[4]))}{chr(int(match[5]))}")
    else:
        print("Valid message not found!")
