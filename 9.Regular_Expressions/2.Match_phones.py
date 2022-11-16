import re

data = input()
pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
# pattern = r"\+359(?P<sep>[-| ])2(?P=sep)\d{3}(?P=sep)\d{4}\b"

phones = re.finditer(pattern, data)
phones = [phone.group(0) for phone in phones]
# print(*phones, sep=",")
print(", ".join(phones))
