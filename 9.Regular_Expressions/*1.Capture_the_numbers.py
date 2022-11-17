import re

while True:
    text = input()
    if not text:
        break
    pattern = r"[0-9]+"
    numbers = re.finditer(pattern, text, flags=re.MULTILINE)

    for number in numbers:
        print(number.group(), end=" ")
