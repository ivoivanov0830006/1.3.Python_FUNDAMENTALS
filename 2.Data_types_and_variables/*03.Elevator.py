total_people = int(input())
capacity = int(input())

total_courses = total_people // capacity
if total_people % capacity != 0:
    total_courses += 1
print(total_courses)
