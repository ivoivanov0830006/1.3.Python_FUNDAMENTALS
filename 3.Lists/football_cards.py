players = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_terminated = False

for player in players:
    element = player.split("-")
    team = element[0]
    number = int(element[1])

    if team == "A":
        if number in team_a:
            team_a.remove(number)
    elif team == "B":
        if number in team_b:
            team_b.remove(number)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")
