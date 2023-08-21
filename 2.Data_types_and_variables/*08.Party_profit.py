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


# --------------------------- Problem to resolve ----------------------------


# As a young adventurer, you travel with your group worldwide, seeking for gold and glory.
# But you need to split the profit among your companions.
# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion
# for drinking water.
#   - Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion,
#     but if you have a motivational party the same day, you spend additional 2 coins per companion.
#   - Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
#     but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You should calculate how many coins gets each companion at the end of the adventure.
# Input / Constraints
# The input will consist of exactly 2 lines:
#   - group size – integer in the range [1…100]
#   - days – integer in the range [1…100]
# Output
#   - Print the following message: "{companions_count} companions received {coins} coins each."
# Note: You cannot split a coin, so you should round down the coins to an integer number.
# Input	                Output
# 3                     3 companions received 90 coins each.
# 5
# --------------------------------------------------------------
# 15                    19 companions received 102 coins each.
# 30
