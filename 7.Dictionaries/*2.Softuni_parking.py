parking = {}

cars_count = int(input())

for cars in range(cars_count):
    current_input = input().split()
    command = current_input[0]

    if command == "register":
        username = current_input[1]
        license_plate = current_input[2]
        if username not in parking.keys():
            parking[username] = license_plate
            print(f"{username} registered {parking[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")

    elif command == "unregister":
        username = current_input[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]


for workers_name, cars_license_plate in parking.items():
    print(f"{workers_name} => {cars_license_plate}")
