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
