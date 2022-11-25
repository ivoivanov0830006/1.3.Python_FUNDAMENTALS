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

        
# ------------------------------------- Problem to resolve -----------------------------------------
#
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can 
# choose for your party. On the next n lines, the heroes themselves will follow with their hit points and 
# mana points separated by a single space in the following format:
#       "{hero name} {HP} {MP}"
# HP stands for hit points and MP for mana points
# a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving 
# different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
#   * "CastSpell – {hero name} – {MP needed} – {spell name}"
# If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
#       "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# If the hero is unable to cast the spell print:
#       "{hero name} does not have enough MP to cast {spell name}!"
#   * "TakeDamage – {hero name} – {damage} – {attacker}"
# Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#       "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# If the hero has died, remove him from your party and print:
#       "{hero name} has been killed by {attacker}!"
#   * "Recharge – {hero name} – {amount}"
# The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased 
# to 200. (the MP can't go over the maximum value).
#  Print the following message:
#       "{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum 
# value (100), HP is increased to 100 (the HP can't go over the maximum value).
#  Print the following message:
#       "{hero name} healed for {amount recovered} HP!"
# Print all members of your party who are still alive, in the following format (their HP/MP need to be 
# indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                                    Output
# 2                                         Solmyr healed for 10 HP!
# Solmyr 85 120                             Solmyr recharged for 50 MP!
# Kyrre 99 50                               Kyrre was hit for 66 HP by Orc and now has 33 HP left!
# Heal - Solmyr - 10                        Kyrre has successfully cast ViewEarth and now has 35 MP!
# Recharge - Solmyr - 50                    Solmyr
# TakeDamage - Kyrre - 66 - Orc               HP: 95
# CastSpell - Kyrre - 15 - ViewEarth          MP: 170
# End	                                    Kyrre
#                                             HP: 33
#                                             MP: 35
# ------------------------------------------------------------------------------------------
# 4                                         SirMullich healed for 30 HP!
# Adela 90 150                              Adela recharged for 50 MP!
# SirMullich 70 40                          Tyris does not have enough MP to cast Fireball!
# Ivor 1 111                                Tyris has been killed by Fireball!
# Tyris 94 61                               Ivor has been killed by Mosquito!
# Heal - SirMullich - 50                    Adela
# Recharge - Adela - 100                      HP: 90
# CastSpell - Tyris - 1000 - Fireball         MP: 200
# TakeDamage - Tyris - 99 - Fireball        SirMullich
# TakeDamage - Ivor - 3 - Mosquito            HP: 100
# End	                                      MP: 40
