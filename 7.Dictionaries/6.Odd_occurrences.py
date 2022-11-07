sequence = input().split()
words_lowercase = []

words = {}

for word in sequence:
    words_lowercase.append(word.lower())

for key in words_lowercase:
    if key not in words.keys():
        words[key] = 0
    words[key] += 1

for key, occurrences in words.items():
    if occurrences % 2 != 0:
        print(f"{key}", end=" ")
