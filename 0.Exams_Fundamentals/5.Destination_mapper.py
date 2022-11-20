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
