import re

input_text = input()
pattern = r"(?P<sep>[#|@])(?P<word_one>[a-zA-Z]{3,})(?P=sep){2}(?P<word_two>[a-zA-Z]{3,})(?P=sep)"
matches = re.findall(pattern, input_text)

mirrored_words = []
valid_pairs_count = 0

for match in matches:
    valid_pairs_count += 1
    word_one = match[1]
    word_two = match[2]

    if word_one == word_two[::-1]:
        mirrored_words.append(word_one)
        mirrored_words.append(word_two)
        # mirrored_words.append(f"{word_one} <=> {word_two}")
final_dict = []

if valid_pairs_count == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{valid_pairs_count} word pairs found!")
    if len(mirrored_words) != 0:
        for index in range(0, len(mirrored_words), 2):
            first_word = mirrored_words[index]
            second_word = mirrored_words[index + 1]
            final_dict.append(first_word + " <=> " + second_word)
        print("The mirror words are:")
        print(", ".join(final_dict))
    else:
        print("No mirror words!")
