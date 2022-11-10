text = input()

digits, letters, other = [], [], []

for symbol in text:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        letters.append(symbol)
    else:
        other.append(symbol)

print("".join(digits))
print("".join(letters))
print("".join(other))
