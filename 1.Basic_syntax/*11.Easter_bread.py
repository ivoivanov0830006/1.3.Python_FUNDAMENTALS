budget = float(input())
flour_price_kg = float(input())
eggs_price_pack = 0.75 * flour_price_kg
milk_price_liter = 1.25 * flour_price_kg
loaf_price = flour_price_kg + eggs_price_pack + milk_price_liter / 4
loaf_count = 0
colored_eggs = 0

while budget > loaf_price:
    budget -= loaf_price
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= (loaf_count - 2)
print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and"
      f" {budget:.2f}BGN left.")
