results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    current_command = command.split("-")
    username, language = current_command[0], current_command[1]
    if language == "banned":
        for key, value in results.items():
            if username in value:
                results[key].pop(username)

    else:
        points = int(current_command[2])
        if language not in results.keys():
            results[language] = {}
            submissions[language] = 1
            if username not in results[language]:
                results[language][username] = points

        else:
            submissions[language] += 1
            if username in results[language]:
                if results[language][username] < points:
                    results[language][username] = points
            elif username not in results[language]:
                results[language][username] = points

print("Results:")
for user in results.values():
    for key, value in user.items():
        print(f"{key} | {value}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
