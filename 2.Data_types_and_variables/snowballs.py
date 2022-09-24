number_balls = int(input())
highest_weight = 0
highest_time = 0
highest_quality = 0
highest_value = 0

for ball in range(number_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = int((weight / time) ** quality)
    if highest_value < value:
        highest_value = value
        highest_quality = quality
        highest_time = time
        highest_weight = weight

print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
