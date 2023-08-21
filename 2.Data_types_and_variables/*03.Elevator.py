total_people = int(input())
capacity = int(input())

total_courses = total_people // capacity
if total_people % capacity != 0:
    total_courses += 1
print(total_courses)


# --------------------------- Another solution ----------------------------

# total_people = int(input())
# capacity = int(input())
# total_courses = 0
#
# rest_people = total_people % capacity
# if rest_people == 0:
#     total_courses = total_people / capacity
# else:
#     total_courses = total_people // capacity + 1
# print(int(total_courses))
