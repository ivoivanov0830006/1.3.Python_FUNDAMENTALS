command = input()
coffee = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee += 2
    else:
        coffee += 0
    command = input()
if coffee > 5:
    print("You need extra sleep")
else:
    print(f"{coffee}")
