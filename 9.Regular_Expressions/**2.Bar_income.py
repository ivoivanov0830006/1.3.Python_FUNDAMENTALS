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


# ------------------------------------- Problem to resolve ------------------------------
#
# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go
# home and you are the person who has to draw the line and calculate the money from the products that were
# sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input.
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by
# lower-case letters
# Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# Valid count is an integer, surrounded by '|'
# Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in
# the following format: "Total income: {income}".
# Input / Constraints
# Strings that you have to process until you receive text "end of shift".
# Output
# Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
# After receiving "end of shift" print the total amount of money for the day rounded to 2 decimal places in
# the following format: "Total income: {income}"
# Allowed working time / memory: 100ms / 16MB.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# %George%<Croissant>|2|10.3$           George: Croissant - 20.60
# %Peter%<Gum>|1|1.3$                   Peter: Gum - 1.30
# %Maria%<Cola>|1|2.4$                  Maria: Cola - 2.40
# end of shift	                        Total income: 24.30
# ------------------------------------------------------------------
# %InvalidName%<Croissant>|2|10.3$      Valid: Valid - 200.00
# %Peter%<Gum>1.3$                      Total income: 200.00
# %Maria%<Cola>|1|2.4
# %Valid%<Valid>valid|10|valid20$
# end of shift
