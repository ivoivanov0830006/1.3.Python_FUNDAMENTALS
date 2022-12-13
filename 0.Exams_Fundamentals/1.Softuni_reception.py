employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
total_students = int(input())
total_hours = 0

total_students_per_hour = employee1 + employee2 + employee3

while total_students > 0:
    total_hours += 1
    if total_hours % 4 == 0:
        continue
    else:
        total_students -= total_students_per_hour


print(f"Time needed: {total_hours}h.")
