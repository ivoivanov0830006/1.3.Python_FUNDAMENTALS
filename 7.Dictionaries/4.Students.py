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
