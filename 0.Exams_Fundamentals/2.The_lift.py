people = int(input())
wagons = input()
new_wagons = ""
is_empty = False

string_wagons = wagons.replace(" ", "")

for wagon in range(len(string_wagons)):
    total_passengers = 0

    digit = int(string_wagons[wagon])
    current_free_seats = 4 - digit
    if people >= current_free_seats:
        people -= current_free_seats
        total_passengers = 4
    else:
        total_passengers = digit + people
        people = 0
        is_empty = True
    new_digit = str(total_passengers)
    new_wagons += new_digit

if is_empty:
    print("The lift has empty spots!")
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
string_wagons = " ".join(new_wagons)
print(string_wagons)


# --------------------------- Problem to resolve -----------------------------
#
# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full,
# you should direct the people to the next one with space available.
# Input
# On the first line, you will receive how many people are waiting to get on the lift
# On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue,
# you should print on the console the final state of the lift's wagons separated by " " and one
# of the following messages:
# If there are no more people and the lift have empty spots, you should print:
#   - "The lift has empty spots!
#     {wagons separated by ' '}"
# If there are still people in the queue and no more available space, you should print:
#   - "There isn't enough space! {people} people in a queue!
#     {wagons separated by ' '}"
# If the lift is full and there are no more people in the queue, you should print only
# the wagons separated by " "
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 15                        The lift has empty spots!
# 0 0 0 0	                4 4 4 3
#
#       First state - 4 0 0 0 -> 11 people left
#       Second state – 4 4 0 0 -> 7 people left
#       Third state – 4 4 4 0 -> 3 people left
#
# --------------------------------------------------------------
# 20                        There isn't enough space! 10 people in a queue!
# 0 2 0	                    4 4 4
#
#       First state - 4 2 0  -> 16 people left
#       Second state – 4 4 0  -> 14 people left
#       Third state – 4 4 4 -> 10 people left, but there a00re no more wagons.
