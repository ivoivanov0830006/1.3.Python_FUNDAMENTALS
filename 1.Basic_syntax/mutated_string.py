word_1 = input()
word_2 = input()
new_word = ""
last_word = ""
n = 1

for char in range(len(word_1)):
    new_word += word_2[:n] + word_1[n:]
    n += 1
    if new_word != word_1 and new_word != last_word:
        print(new_word)
        last_word = new_word
        new_word = ""
    else:
        last_word = ""
        continue
