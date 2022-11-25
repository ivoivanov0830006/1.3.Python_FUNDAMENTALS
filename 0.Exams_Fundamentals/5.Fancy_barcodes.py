import re

barcodes_count = int(input())
all_products = []
for _ in range(barcodes_count):
    current_product = input()
    all_products.append(current_product)

all_matches = {}

input_text = " ".join(all_products)
pattern_product = r"(@#+(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+)"
matches = re.findall(pattern_product, input_text)
for match in matches:
    product = match[0]
    group_number = ""
    count = 0
    for char in product:
        if char.isdigit():
            group_number += char
            count += 1
    if count == 0:
        group_number = "00"
    all_matches[product] = group_number

for product in all_products:
    if product not in all_matches:
        print("Invalid barcode")
    else:
        print(f"Product group: {all_matches[product]}")


# ------------------------------------- Another Solution -----------------------------
#
# import re
#
# barcodes_count = int(input())
# pattern_product = r"(@#+)(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
#
# for _ in range(barcodes_count):
#     current_product = input()
#     match = re.search(pattern_product, current_product)
#
#     if match:
#         product = match.group(2)
#         pattern_number = r"\d+"
#         group_match = re.findall(pattern_number, product)
#
#         if group_match:
#             product_group = ""
#             for number in group_match:
#                 product_group += number
#             print(f"Product group: {product_group}")
#         else:
#             print("Product group: 00")
#     else:
#         print("Invalid barcode")


# ------------------------------------- Problem to resolve -----------------------------------------
#
# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# It is surrounded by a "@" followed by one or more "#"
# It is at least 6 characters long (without the surrounding "@" or "#")
# It starts with a capital letter
# It contains only letters (lower and upper case) and digits
# It ends with a capital letter
#   * Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
#   * Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
# Next, you have to determine the product group of the item from the barcode. The product group is obtained
# by concatenating all the digits found in the barcode. If there are no digits present in the barcode, the
# default product group is "00". For example:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46
# On the first line, you will be given an integer n – the count of barcodes that you will be receiving next.
# On the following n lines, you will receive different strings. For each barcode that you process, you need
# to print a message.
# If the barcode is invalid:
#       "Invalid barcode"
# If the barcode is valid:
#       "Product group: {product group}"
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# 3                             Product group: 00
# @#FreshFisH@#                 Product group: 0
# @###Brea0D@###                Product group: 46
# @##Che4s6E@##
# ---------------------------------------------------
# 6                             Product group: 11
# @###Val1d1teM@###             Product group: 00
# @#ValidIteM@#                 Invalid barcode
# ##InvaliDiteM##               Invalid barcode
# @InvalidIteM@                 Invalid barcode
# @#Invalid_IteM@#              Product group: 00
# @#ValiditeM@#

