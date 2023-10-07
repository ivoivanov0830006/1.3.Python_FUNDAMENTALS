def average(total_sum, grades_count):
    return total_sum / grades_count


academy = {}
count = int(input())

for _ in range(count):

    name = input()
    grade = float(input())
    if name not in academy.keys():
        academy[name] = []
    academy[name].append(grade)

for key, value in academy.items():
    average_grade = average(sum(value),len(value))
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")

        
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher
# than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
#       "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 5                         John -> 5.00
# John                      Alice -> 4.50
# 5.5                       George -> 5.00
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
# ----------------------------------------------
# 5                         Rob -> 5.50
# Amanda                    Christian -> 5.00
# 3.5                       Robert -> 6.00
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6
