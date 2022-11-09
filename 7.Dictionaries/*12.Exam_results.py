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
    
    
# ------------------------------------- Problem to resolve ------------------------------
#
# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the
# task of taking all the submissions and analyzing them properly. You should collect all the submissions
# and print the final results and statistics about each language in which the participants submitted their
# solutions.
# You will be receiving lines in the following format:
#       "{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and their submissions and points. If a student has two or
# more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that
# case, you should remove the user from the contest but preserve his submissions in the total count of
# submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
#       "{username}-{language}-{points}"
# You can receive a ban command ->
#       "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# Print the exam results for each participant
# After that, print each language in the format shown above
# Allowed working time / memory: 100ms / 16MB
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# Peter-Java-84                 Results:
# George-C#-70                  Peter | 84
# George-C#-84                  George | 84
# Katy-C#-94                    Katy | 94
# exam finished	                Submissions:
#                               Java - 1
#                               C# - 3
# ------------------------------------------
# Peter-Java-91                 Results:
# George-C#-84                  Peter | 91
# Katy-Java-90                  George | 84
# Katy-C#-50                    Submissions:
# Katy-banned                   Java - 2
# exam finished	                C# - 2
