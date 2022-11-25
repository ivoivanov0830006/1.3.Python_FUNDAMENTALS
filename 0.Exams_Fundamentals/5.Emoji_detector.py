import re

input_text = input()
# emoji_pattern = r"((?P<sep>\*{2}|:{2})(?P<word>[A-Z][a-z][a-z]+)(?P=sep))"
emoji_pattern = r"((?P<sep>\*{2}|:{2})(?P<word>[A-Z]{1}[a-z]{2,})(?P=sep))"
threshold_pattern = r"\d"

matches = re.findall(emoji_pattern, input_text)
numbers = re.findall(threshold_pattern, input_text)

threshold_result = 1
for num in numbers:
    threshold_result *= int(num)

emoji_count = len(matches)

print(f"Cool threshold: {threshold_result}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")

for match in matches:
    emoji = match[0]
    word_value = sum(ord(ch) for ch in match[2])
    if word_value >= threshold_result:
        print(emoji)

  
# ------------------------------------- Problem to resolve -----------------------------------------
#
# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
# It is surrounded by 2 characters, either "::" or "**"
# It is at least 3 characters long (without the surrounding symbols)
# It starts with a capital letter
# Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is
# determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text,
# count them and print only the cool ones on the console.
# Input
# On the single input, you will receive a piece of string.
# Output
# On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
# On the following line, print the count of all emojis found in the text in format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"
# Constraints
# There will always be at least one digit in the text!
# -------------------------------------- Example inputs ----------------------------------
# Input
# In the Sofia Zoo there are 311 animals in total!
# ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and
# 21 different types of :Snak::Es::. ::Mooning:: **Shy**
# Output
# Cool threshold: 540
# 4 emojis found in the text. The cool ones are:
# ::Smiley::
# **Tigers**
# ::Mooning::
# ------------------------------------------------------------------
# Input
# 5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun!
# ::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::
# Output
# Cool threshold: 120
# 4 emojis found in the text. The cool ones are:
# ::Joy::
# **Banana**
# ::Wink::
# **Vali**
# -------------------------------------------------------------------
# Input
# It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when
# looking at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution
# of 8 letters, as opposed to using 'Content here, content 99 here', making it look like readable **English**.
# Output
# Cool threshold: 17496
# 1 emojis found in the text. The cool ones are:
