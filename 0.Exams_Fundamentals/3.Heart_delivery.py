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

    
# --------------------------- Problem to resolve -----------------------------
#
# You will receive a string with even integers, separated by a "@" - this is our neighborhood.
# After that, a series of Jump commands will follow until you receive "Love!". Every house in
# the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate
# Valentine's day. The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house (index 0) and must jump by a given length.
# The jump commands will be in this format: "Jump {length}".
# Every time he jumps from one house to another, the needed hearts for the visited house are
# decreased by 2:
#   * If the needed hearts for a certain house become equal to 0, print on the console:
#                   "Place {house_index} has Valentine's day."
#   * If Cupid jumps to a house where the needed hearts are already 0, print on the console:
#                   "Place {house_index} already had Valentine's day."
#   * Keep in mind that Cupid can have a larger jump length than the size of the neighborhood,
#   and if he does jump outside of it, he should start from the first house again (index 0)
# Input
#   * On the first line, you will receive a string with even integers separated by "@" –
# the neighborhood and the number of hearts for each house.
#   * On the next lines, until "Love!" is received, you will be getting jump commands in this
#   format: "Jump {length}".
# Output
# In the end, print Cupid's last position and whether his mission was successful or not:
#   * "Cupid's last position was {last_position_index}."
#   * If each house has had Valentine's day, print: "Mission was successful."
#   * If not, print the count of all houses that didn't celebrate: "Cupid has failed {houseCount} places."
# Constraints
#   * The neighborhood's size will be in the range [1…20]
#   * Each house will need an even number of hearts in the range [2 … 10]
#   * Each jump length will be an integer in the range [1 … 20]
# Input	                        Output
# 10@10@10@2                    Place 3 has Valentine's day.
# Jump 1                        Cupid's last position was 3.
# Jump 2                        Cupid has failed 3 places.
# Love!
# ---------------------------------------------------------------
# 2@4@2                         Place 2 has Valentine's day.
# Jump 2                        Place 0 has Valentine's day.
# Jump 2                        Place 0 already had Valentine's day.
# Jump 8                        Place 0 already had Valentine's day.
# Jump 3                        Cupid's last position was 1.
# Jump 1                        Cupid has failed 1 places.
# Love!
