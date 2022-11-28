import re

number_lines = int(input())
pattern_letters = r"[sStTaArR]"
decrypted_messages = []

for _ in range(number_lines):
    input_text = input()
    key = len(re.findall(pattern_letters, input_text))
    new_message = ""
    for char in input_text:
        new_char = ord(char) - int(key)
        new_message += chr(new_char)
    decrypted_messages.append(new_message)

pattern = r"@(?P<name>[A-Za-z]+)[^@:!>-]*:(?P<population>\d+)[^@:!>-]*!(?P<attack>[A|D])![^@:!>-]*->(?P<soldiers>\d+)"
attacked_planets = []
destroyed_planets = []

for message in decrypted_messages:
    match = re.search(pattern, message)
    if match:
        planet_name = match.group(1)
        population = match.group(2)
        action = match.group(3)
        soldiers = match.group(4)
        if action == "A":
            attacked_planets.append(planet_name)
        elif action == "D":
            destroyed_planets.append(planet_name)

attacked_planets = sorted(attacked_planets)
destroyed_planets = sorted(destroyed_planets)

print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for attacked_planet in attacked_planets:
        print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for destroyed_planet in destroyed_planets:
        print(f"-> {destroyed_planet}")

