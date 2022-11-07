products = list(input().split())
needed_products = input().split()
stock = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    stock[key] = int(value)

for product in needed_products:
    if product in stock.keys():
        quantity = stock[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Now not only you have to keep track of the stock, but also you should answer customers if you have some
# products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2
# possibilities:
#   ⦁	If you have the product, print "We have {quantity} of {product} left".
#   ⦁	Otherwise, print "Sorry, we don't have {product}".
# -------------------------------------- Example inputs ----------------------------------
# Input	                                        Output
# cheese 10 bread 5 ham 10 chocolate 3          Sorry, we don't have jam
# jam cheese ham tomatoes	                    We have 10 of cheese left
#                                               We have 10 of ham left
#                                               Sorry, we don't have tomatoes
# ---------------------------------------------------------------------------
# eggs 5 bread 10                               We have 10 of bread left
# bread eggs	                                We have 5 of eggs left
