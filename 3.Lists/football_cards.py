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
    
    
# --------------------------- Another solution ----------------------------
#
# players = input().split()
#
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# is_terminated = False
#
# for player in players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_a.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         is_terminated = True
#         break
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if is_terminated:
#     print("Game was terminated")
#
# --------------------------- Problem to resolve -----------------------------
#
# Most football fans love it for the goals and excitement. Well, this problem does not. You are up to
# handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered
# from 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams
# has less than 7 players remaining, the referee stops the game immediately, and the team with less
# than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the
# player's number. e.g., the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space.
# You should print the count of remaining players on each team at the end of the game in the format:
# "Team A - {players_count}; Team B - {players_count}". If the referee terminated the game, print
# an additional line: "Game was terminated".
