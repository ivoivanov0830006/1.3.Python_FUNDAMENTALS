days = int(input())
players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_food = days * food_per_day * players
total_water = days * water_per_day * players

previous_water = 0
previous_food = 0

no_energy = False

for day in range(1, days + 1):
    previous_water = total_water
    previous_food = total_food
    energy_loss = float(input())
    group_energy -= energy_loss

    if day % 2 == 0:  # (watering day)
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:  # (eating day)
        group_energy += group_energy * 0.1
        total_food -= total_food / players
    if group_energy <= 0:
        no_energy = True
        break

if no_energy:
    print(f"You will run out of energy. You will be left with {previous_food:.2f} food and {previous_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
