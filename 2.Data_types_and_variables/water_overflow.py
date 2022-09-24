number_fillings = int(input())
tank_capacity = 255
total_capacity = 0

for _ in range(number_fillings):
    water_input = int(input())
    if tank_capacity - water_input < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= water_input
    total_capacity += water_input
print(total_capacity)
