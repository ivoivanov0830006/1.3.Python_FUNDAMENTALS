number_lines = int(input())

# constant values
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

numbers = []

for _ in range(number_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []

# numbers filtering
for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)


# --------------------------- Another solution ----------------------------
#
# number = int(input())
# numbers = []
# filtered = []
#
# for _ in range(number):
#     current_number = int(input())
#     numbers.append(current_number)
# command = input()
# if command == "even":
#     for number in numbers:
#         if number % 2 == 0:
#             filtered.append(number)
# elif command == "odd":
#     for number in numbers:
#         if number % 2 != 0:
#             filtered.append(number)
# elif command == "negative":
#     for number in numbers:
#         if number < 0:
#             filtered.append(number)
# elif command == "positive":
#     for number in numbers:
#         if number >= 0:
#             filtered.append(number)
# print(filtered)


# --------------------------- Problem to resolve -----------------------------
#
# On the first line, you will receive a single number n. On the following n lines, you will
# receive integers. After that, you will be given one of the following commands:
# ⦁	even
# ⦁	odd
# ⦁	negative
# ⦁	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even).
# Finally, print the result.
# Input	                    Output
# 5                         [-2, 18, 998]
# 33
# 19
# -2
# 18
# 998
# even
# -----------------------------------------------
# 3                         [-4]
# 111
# -4
# 0
# negative
