food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
everything_enough = True

food_per_day = 0.3

for day in range(1, 31):
    food -= food_per_day
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        everything_enough = False
        break

if everything_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
