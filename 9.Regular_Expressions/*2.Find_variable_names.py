import re

text = input()
pattern = r"(?P<underscore>\b_{1})(?P<text>[a-zA-Z0-9]+\b)"

results = re.finditer(pattern, text)
valid_strings = []

for result in results:
    valid_strings.append(result[2])

print(",".join(valid_strings))
