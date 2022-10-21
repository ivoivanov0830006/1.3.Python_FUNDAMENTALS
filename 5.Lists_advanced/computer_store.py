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


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that prints you a receipt for your new computer. You will receive the
# parts' prices (without tax) until you receive what type of customer this is - special or regular.
# Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!" on the console and
# continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.
# Input
#   - You will receive numbers representing prices (without tax) until command "special" or "regular":
# Output
#   - The receipt should be in the following format:
#       "Congratulations you've just bought a new computer!
#       Price without taxes: {total price without taxes}$
#       Taxes: {total amount of taxes}$
#       -----------
#       Total price: {total price with taxes}$"
# Note: All prices should be displayed to the second digit after the decimal point!
# The discount is applied only on the total price. Discount is only applicable to the final price!
# Input	                            Output
# 1050                              Congratulations you've just bought a new computer!
# 200                               Price without taxes: 1737.36$
# 450                               Taxes: 347.47$
# 2                                 -----------
# 18.50                             Total price: 1876.35$
# 16.86
# special
