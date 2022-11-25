number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    name, health, mana = input().split()
    heroes[name] = {}
    heroes[name]["HP"] = int(health)
    heroes[name]["MP"] = int(mana)

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split(" - ")
    action = current_command[0]

    if action == "CastSpell":
        name = current_command[1]
        needed_mana = int(current_command[2])
        spell = current_command[3]
        if heroes[name]["MP"] >= needed_mana:
            heroes[name]["MP"] -= needed_mana
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif action == "TakeDamage":
        name = current_command[1]
        damage = int(current_command[2])
        attacker = current_command[3]
        if heroes[name]["HP"] > damage:
            heroes[name]["HP"] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]

    elif action == "Recharge":
        name = current_command[1]
        mana_amount = int(current_command[2])
        heroes[name]["MP"] += mana_amount
        if heroes[name]["MP"] > 200:
            diff = abs(heroes[name]["MP"] - 200 - mana_amount)
            heroes[name]["MP"] = 200
            print(f"{name} recharged for {diff} MP!")
        else:
            print(f"{name} recharged for {mana_amount} MP!")

    elif action == "Heal":
        name = current_command[1]
        health_amount = int(current_command[2])
        heroes[name]["HP"] += health_amount
        if heroes[name]["HP"] > 100:
            diff = abs(heroes[name]["HP"] - 100 - health_amount)
            heroes[name]["HP"] = 100
            print(f"{name} healed for {diff} HP!")
        else:
            print(f"{name} healed for {health_amount} HP!")

if len(heroes) > 0:
    for name in heroes:
        health = heroes[name]["HP"]
        mana = heroes[name]["MP"]
        print(f"""{name}
  HP: {health}
  MP: {mana}""")
