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
