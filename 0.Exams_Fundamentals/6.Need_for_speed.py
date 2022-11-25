number_of_cars = int(input())

race = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    race[car] = {}
    race[car]["Mileage"] = int(mileage)
    race[car]["Fuel"] = int(fuel)


while True:
    command = input()
    if command == "Stop":
        break

    current_command = command.split(" : ")
    action = current_command[0]

    if action == "Drive":
        car = current_command[1]
        distance = int(current_command[2])
        fuel = int(current_command[3])
        if race[car]["Fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            race[car]["Mileage"] += distance
            race[car]["Fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if race[car]["Mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del race[car]

    elif action == "Refuel":
        car = current_command[1]
        fuel = int(current_command[2])
        maximum = 75
        if race[car]["Fuel"] + fuel > maximum:
            diff = abs(maximum - race[car]["Fuel"])
            race[car]["Fuel"] = maximum
            print(f"{car} refueled with {diff} liters")
        else:
            race[car]["Fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        car = current_command[1]
        kilometers = int(current_command[2])
        if race[car]["Mileage"] - kilometers < 10000:
            race[car]["Mileage"] = 10000
        else:
            race[car]["Mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in race:
    mileage = race[car]["Mileage"]
    fuel = race[car]["Fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
