to_remove = input()
word = input()

while to_remove in word:
    word = word.replace(to_remove, "")

print(word)
