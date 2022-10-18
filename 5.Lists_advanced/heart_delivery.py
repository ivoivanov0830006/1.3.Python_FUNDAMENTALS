neighbourhood = list(map(int, input().split("@")))
position = 0
cmd = input()

while cmd != "Love!":
    command = cmd.split(" ")
    jump_length = int(command[1])
    position += jump_length
    if position >= len(neighbourhood):
        position = 0
    if neighbourhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighbourhood[position] -= 2
        if neighbourhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    cmd = input()

print(f"Cupid's last position was {position}.")

if sum(neighbourhood) == 0:
    print("Mission was successful.")

else:
    places_to_visit = [hearts for hearts in neighbourhood if hearts != 0]
    print(f"Cupid has failed {len(places_to_visit)} places.")

