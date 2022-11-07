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
