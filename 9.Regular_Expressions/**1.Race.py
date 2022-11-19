import re
competition = {}
competitors = input().split(", ")
for competitor in competitors:
    if competitor not in competition:
        competition[competitor] = 0

pattern_letters = r"[a-zA-Z]"
pattern_numbers = r"\d"

while True:
    command = input()
    if command == "end of race":
        break

    name = "".join(re.findall(pattern_letters, command))
    distance = re.findall(pattern_numbers, command)
    total_distance = sum(int(number) for number in distance)
    if name in competition.keys():
        competition[name] += total_distance

competition_sorted = sorted(competition, key=competition.get, reverse=True)

print(f"1st place: {competition_sorted[0]}")
print(f"2nd place: {competition_sorted[1]}")
print(f"3rd place: {competition_sorted[2]}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that processes information about a race. On the first line you will be given list of
# participants separated by ", ". On the next few lines until you receive a line "end of race" you will
# be given some info which will be some alphanumeric characters. In between them you could have some
# extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". The letters are the
# name of the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person. If you
# receive the same person more than once just add the distance to his old distance. At the end print the
# top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                    Output
# George, Peter, Bill, Tom                  1st place: George
# G4e@55or%6g6!68e!!@                       2nd place: Peter
# R1@!3a$y4456@                             3rd place: Tom
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race
