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
