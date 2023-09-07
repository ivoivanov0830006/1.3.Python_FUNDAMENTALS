def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
palindrome = input()
palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")

# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line, you will receive words separated by a single space. On the second line,
# you will receive a palindrome. First, you should print a list containing all the found palindromes
# in the sequence. Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".
# Input	                                    Output
# wow father mom wow shirt stats            ['wow', 'mom', 'wow', 'stats']
# wow	                                    Found palindrome 2 times
# ----------------------------------------------------------------------------
# hey how you doin? lol                     Found palindrome 0 times
# mom	['lol']
