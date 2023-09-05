def orders(order):
    if order == "coffee":
        return quantity * coffee_price
    elif order == "water":
        return quantity * water_price
    elif order == "coke":
        return quantity * coke_price
    elif order == "snacks":
        return quantity * snacks_price


current_order = input()
quantity = int(input())
coffee_price = 1.5
water_price = 1
coke_price = 1.4
snacks_price = 2
total = orders(current_order)
print(f"{total:.2f}")

# ------------------------------------- Another solution -------------------------------

# def orders(order, quantity):
#     price = 0
#     coffee_price = 1.5
#     water_price = 1
#     coke_price = 1.4
#     snacks_price = 2
#     if order == "coffee":
#         price = quantity * coffee_price
#     elif order == "water":
#         price = quantity * water_price
#     elif order == "coke":
#         price = quantity * coke_price
#     elif order == "snacks":
#         price = quantity * snacks_price
#     return price
#
#
# current_order = input()
# current_quantity = int(input())
#
# total = orders(current_order, current_quantity)
# print(f"{total:.2f}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a function that calculates the total price of an order and returns it. The function should
# receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of
# the product. The prices for a single piece of each product are:
#   ⦁	coffee - 1.50
#   ⦁	water - 1.00
#   ⦁	coke - 1.40
#   ⦁	snacks - 2.00
# Print the result formatted to the second decimal place.
# Input	                Output
# water                 5.00
# 5
# -------------------------------
# coffee                3.00
# 2
