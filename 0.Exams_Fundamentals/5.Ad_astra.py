import re

resources = input()

pattern = r"(?P<sep>#|\|)(?P<item>[A-Za-z\ ]+)(?P=sep)(?P<date>\d{2}/\d{2}/\d{2})(?P=sep)(?P<calories>\d+)(?P=sep)"

matches = re.findall(pattern, resources)
total_calories = sum(int(match[3]) for match in matches)
total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")


for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
