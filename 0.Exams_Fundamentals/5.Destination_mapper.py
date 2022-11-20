import re

valid_locations = []
travel_points = 0

locations = input()
pattern = r"(?P<sep>[=|\/])(?P<place>[A-Z][A-Za-z][A-Za-z]+)(?P=sep)"

matches = re.findall(pattern, locations)
for match in matches:
    valid_locations.append(match[1])
    travel_points += len(match[1])

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given a string representing some places on the map. You have to filter only the valid ones.
# A valid location is:
#       * Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
#       * After the first "=" or "/" there should be only letters (the first must be upper-case, other letters
#       could be upper or lower-case)
#       * The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two
# locations are valid.
# After you have matched all the valid locations, you have to calculate travel points. They are calculated
# by summing the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print:
#       * "Destinations: {destinations joined by ', '}".
#       * On the second line, print "Travel Points: {travel_points}".
# -------------------------------------- Example inputs ----------------------------------
# Input	                                                    Output
# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=	    Destinations: Hawai, Cyprus
#                                                           Travel Points: 11
# --------------------------------------------------------------------------------------
# ThisIs some InvalidInput	                                Destinations:
#                                                           Travel Points: 0
