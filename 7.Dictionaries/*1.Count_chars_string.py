# text = "".join(input().split())
text = input().replace(" ", "")

letters = {}

for char in text:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")
