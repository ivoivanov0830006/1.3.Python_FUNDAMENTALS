import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, data)
numbers = [number.group() for number in numbers]

print(*numbers)
