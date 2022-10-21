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


# ------------------------------------- Another Solution -----------------------------
#
# import math
# students = int(input())
# lectures = int(input())
# bonus = int(input())
# all_students = []
# all_attendances = []
#
# for student in range(1, students + 1):
#     attendances = int(input())
#     total_bonus = math.ceil(attendances / lectures * (5 + bonus))
#     all_students.append(total_bonus)
#     all_attendances.append(attendances)
#
# max_bonus = max(all_students)
# index = all_students.index(max_bonus)
#
# print(f"Max Bonus: {max_bonus}.")
# print(f"The student has attended {all_attendances[index]} lectures.")


# ----------------------------------- Problem to resolve -----------------------------
#
# Create a program that calculates bonus points for each student enrolled in a course.
# On the first line, you are going to receive the number of the students. On the second line,
# you will receive the total number of lectures in the course. The course has an additional bonus,
# which you will receive on the third line. On the following lines, you will be receiving the
# count of attendances for each student.
# The bonus is calculated with the following formula:
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print them, along with his attendances, in the
# following format:
# "Max Bonus: {max bonus points}."
# "The student has attended {student attendances} lectures."
# Round the bonus points at the end to the nearest larger number.
# Input / Constrains
# On the first line, you are going to receive the number of the students – an integer in the range [0…50]
# On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
# On the third line, you will receive the additional bonus – an integer number in the range [0….100].
# On the following lines, you will be receiving the attendance of each student.
# There will never be students with equal bonuses.
# Output
# Print the maximum bonus points and the attendances of the given student, rounded to the nearest
# larger number, scored by a student in this course in the format described above.
# Input	                Output
# 5                     Max Bonus: 34.
# 25                    The student has attended 24 lectures.
# 30
# 12
# 19
# 24
# 16
# 20
