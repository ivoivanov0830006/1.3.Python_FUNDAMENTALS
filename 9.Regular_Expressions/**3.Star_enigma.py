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


# ------------------------------------- Problem to resolve -------------------------------
#
# The war is in its peak, but you, young Padwan, can turn the tides with your programming skills. You are tasked
# to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt
# the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and remove
# the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and
# soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# The first line holds n – the number of messages– integer in range [1…100];
# On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                    Output
# 2                                         Attacked planets: 1
# STCDoghudd4=63333$D$0A53333               -> Alderaa
# EHfsytsnhf?8555&I&2C9555SR                Destroyed planets: 1
#                                           -> Cantonica
# --------------------------------------------------------------
# 3                                         Attacked planets: 0
# tt(''DGsvywgerx>6444444444%H%1B9444       Destroyed planets: 2
# GQhrr|A977777(H(TTTT                      -> Cantonica
# EHfsytsnhf?8555&I&2C9555SR	            -> Coruscant
