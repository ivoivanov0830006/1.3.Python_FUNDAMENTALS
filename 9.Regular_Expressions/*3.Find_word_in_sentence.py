import re

text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"
result = len(re.findall(pattern, text, re.IGNORECASE))
print(result)
