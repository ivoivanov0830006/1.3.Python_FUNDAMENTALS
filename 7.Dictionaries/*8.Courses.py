courses = {}

while True:
    command = input()
    if command == "end":
        break
    course, name = command.split(" : ")
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(name)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for values in courses[key]:
        print(f"-- {values}")

        
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
# For each course, print the registered users.
# Input
# Until the "end" command is received, you will be receiving input lines in the format:
#       "{course_name} : {student_name}"
# The product data is always delimited by " : "
# Output
# Print the information about each course in the following format:
#       "{course_name}: {registered_students}"
# Print the information about each student in the following format:
#       "-- {student_name}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                            Output
# Programming Fundamentals : John Smith             Programming Fundamentals: 2
# Programming Fundamentals : Linda Johnson          -- John Smith
# JS Core : Will Wilson                             -- Linda Johnson
# Java Advanced : Harrison White                    JS Core: 1
# end	                                            -- Will Wilson
#                                                   Java Advanced: 1
#                                                   -- Harrison White
# --------------------------------------------------------------------------------
# Algorithms : Jay Moore                            Algorithms: 2
# Programming Basics : Martin Taylor                -- Jay Moore
# Python Fundamentals : John Anderson               -- Bob Jackson
# Python Fundamentals : Andrew Robinson             Programming Basics: 1
# Algorithms : Bob Jackson                          -- Martin Taylor
# Python Fundamentals : Clark Lewis                 Python Fundamentals: 3
# end	                                            -- John Anderson
#                                                   -- Andrew Robinson
#                                                   -- Clark Lewis
