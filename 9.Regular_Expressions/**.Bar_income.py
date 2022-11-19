import re

pattern = r"%(?P<name>[A-Z][a-z]+\b)%[^\|\$\%\.]*<(?P<item>\w+)>[^\|\$\%\.]*\|(?P<quantity>\d+)\|[^\|\$\%\.\d]*" \
          r"(?P<price>\d+(\.\d+)?)\$"
total_sum = 0

while True:
    command = input()
    if command == "end of shift":
        break
    match = re.search(pattern, command)
    if match:
        current_name = match.group(1)
        current_item = match.group(2)
        current_quantity = match.group(3)
        current_price = match.group(4)
        current_sum = int(current_quantity) * float(current_price)
        print(f"{current_name}: {current_item} - {current_sum:.2f}")

        total_sum += current_sum

print(f"Total income: {total_sum:.2f}")
