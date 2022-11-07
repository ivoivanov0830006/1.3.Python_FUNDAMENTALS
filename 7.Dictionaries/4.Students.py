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

