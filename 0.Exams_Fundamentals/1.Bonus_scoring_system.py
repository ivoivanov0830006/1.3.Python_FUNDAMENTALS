import math
students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
max_attendances = 0

for student in range(1, students + 1):
    attendances = int(input())
    current_bonus = math.ceil(attendances / lectures * (5 + bonus))
    if current_bonus >= max_bonus:
        max_bonus = current_bonus
        max_attendances = attendances

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendances} lectures.")
