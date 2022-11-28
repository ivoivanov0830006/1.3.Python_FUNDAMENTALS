import re

demons = []

input_text = input()
name_pattern = r"(?P<name>([^, ])+)"
matches = re.finditer(name_pattern, input_text)

for match in matches:
    group = match.groupdict()
    demons.append(group["name"])

demons = sorted(demons)

for demon_name in demons:
    health_pattern = r"([^*+,-\/.0123456789])"
    health_items = re.findall(health_pattern, demon_name)
    total_health = 0
    for char in health_items:
        total_health += ord(char)

    damage_pattern = r"([+|-]?\d+\.?\d*)"
    damage_items = re.findall(damage_pattern, demon_name)
    total_damage = 0

    for num in damage_items:
        if "." in num:
            total_damage += float(num)
        else:
            total_damage += int(num)

    for symbol in demon_name:
        if symbol == "*":
            total_damage *= 2
        elif symbol == "/":
            total_damage /= 2

    print(f"{demon_name} - {total_health} health, {total_damage:.2f} damage")
