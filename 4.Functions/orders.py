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
