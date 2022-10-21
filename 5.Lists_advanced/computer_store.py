command = input()
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

while command != "regular" or command != "special":
    if command == "regular":
        total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes
        break
    elif command == "special":
        total_price_with_taxes = (total_price_without_taxes + total_amount_of_taxes) * 0.9
        break
    else:
        price = float(command)
        if price < 0:
            print("Invalid price!")
            price = 0
    total_price_without_taxes += price
    total_amount_of_taxes = total_price_without_taxes * 0.2
    command = input()

if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
