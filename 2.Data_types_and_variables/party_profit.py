from math import floor
group = int(input())
days = int(input())
money = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5
    money += 50 - (2 * group)
    if day % 3 == 0:
        money -= 3 * group
    if day % 5 == 0:
        money += 20 * group
        if day % 3 == 0:
            money -= 2 * group
money_per_person = floor(money / group)
print(f"{group} companions received {money_per_person} coins each.")
