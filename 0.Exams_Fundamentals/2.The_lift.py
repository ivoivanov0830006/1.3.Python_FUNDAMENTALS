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
