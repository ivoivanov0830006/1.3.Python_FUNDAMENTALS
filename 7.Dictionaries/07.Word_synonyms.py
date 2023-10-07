dictionary = {}
max_words = int(input())

while max_words > 0:
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    if synonym not in dictionary[word]:
        dictionary[word].append(synonym)
        max_words -= 1

for key, value in dictionary.items():
    value_list = ", ".join(value)
    print(f"{key} - {value_list}")

    
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word.
# The value will be a list of all the synonyms of that word. You will be given a number n – the count of
# the words. After each term, you will be given a synonym, so the count of lines you should read from
# the console is 2 * n. You will be receiving a word and a synonym each on a separate line like this:
# ⦁	{word}
# ⦁	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# 4                                     cute - adorable, charming
# cute                                  smart - clever
# adorable
# cute
# charming
# smart
# clever
# -----------------------------------------------------------------
# 2                                     task – problem, assignment
# task
# problem
# task
# assignment
