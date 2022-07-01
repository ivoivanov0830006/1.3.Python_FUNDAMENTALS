sold_count = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(1, sold_count + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

percentage_heart = hearthstone / sold_count * 100
percentage_for = fornite / sold_count * 100
percentage_over = overwatch / sold_count * 100
percentage_others = others / sold_count * 100
print(f"Hearthstone - {percentage_heart:.2f}%")
print(f"Fornite - {percentage_for:.2f}%")
print(f"Overwatch - {percentage_over:.2f}%")
print(f"Others - {percentage_others:.2f}%")
