words = input().split()
new_word = ""

for word in words:
    new_word += word * len(word)

print(new_word)
