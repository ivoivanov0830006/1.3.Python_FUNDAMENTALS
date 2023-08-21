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


# --------------------------- Another solution ----------------------------

# import math
# total_people = int(input())
# capacity = int(input())
#
# total_courses = math.ceil(total_people / capacity)
#
# print(total_courses)


# --------------------------- Problem to resolve ----------------------------
#
# Calculate how many courses will be needed to elevate N persons by using an elevator with
# a capacity of P persons. The input holds two lines: the number of people N and the
# capacity P of the elevator.
# Input         	Output                  Comments
# 17                6                       5 courses * 3 people
# 3		                                    + 1 course * 2 persons
# -----------------------------------------------------------------------------------
# 4                 1                       All the persons fit inside the elevator.
# 5		                                    Only one course is needed.
# ------------------------------------------------------------------------------------
# 10                2	                    2 courses * 5 people
# 5

