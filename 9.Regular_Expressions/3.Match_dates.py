import re

data = input()
pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
dates = re.finditer(pattern, data)

for date in dates:
    current_object = date.group()
    day = current_object[0:2]
    month = current_object[3:6]
    year = current_object[-4:]

    print(f"Day: {day}, Month: {month}, Year: {year}")
