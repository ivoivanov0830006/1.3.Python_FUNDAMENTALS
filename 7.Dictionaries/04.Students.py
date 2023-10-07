students = {}
command = input().split(":")

while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
    command = input().split(":")

searched_course = command[0].replace("_", "")

# print("\n".join(students[searched_course])
for student in students[searched_course]:
    print(student)


# ------------------------------------- Another Solution -----------------------------
#
# students = {}
# command = input()
#
# while ":" in command:
#     current_command = command.split(":")
#     name, id, course = current_command[0], current_command[1], current_command[2]
#     if course not in students.keys():
#         students[course] = {}
#     students[course][id] = name
#     command = input()
#
# course = " ".join(command.split("_"))
#
# for key, value in students.items():
#     if key == course:
#         for id, name in value.items():
#             print(f"{name} - {id}")


# ------------------------------------- Another Solution -----------------------------
#
# courses = {}
#
# while True:
#     command = list(map(str, input().split(":")))
#     if len(command) == 1:
#         break
#     names_id = []
#     name, identification, course = command[0], command[1], command[2]
#     names_id.append(name)
#     names_id.append(int(identification))
#     if course not in courses.keys():
#         courses[course] = []
#     courses[course] += names_id
#
# searched_course = command[0].replace("_", " ")
#
# for index in range(0, len(courses[searched_course]), 2):
#     key = courses[searched_course][index]
#     value = courses[searched_course][index + 1]
#     print(f"{key} - {value}")


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be receiving names of students, their ID, and a course of programming they have taken
# in the format "{name}:{ID}:{course}". On the last line, you will receive a name of a course in
# snake case lowercase letters. You should print only the information of the students who have
# taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# Peter:123:programming basics          John - 5622
# John:5622:fundamentals                Maya - 89
# Maya:89:fundamentals                  Lilly - 633
# Lilly:633:fundamentals
# fundamentals
# ----------------------------------------------------------------------------------------
# Alex:6:programming basics             Alex - 6
# Maria:7:programming basics            Maria - 7
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
