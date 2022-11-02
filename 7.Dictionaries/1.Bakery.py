products = list(input().split())
bakery = {}

key_list = []
value_list = []


for index in range(len(products)):
    if index % 2 != 0:
        value = int(products[index])
        value_list.append(value)
    else:
        key = products[index]
        key_list.append(key)

bakery = {key_list[index]: value_list[index] for index in range(len(key_list))}
print(bakery)


# ------------------------------------- Another Solution -----------------------------
#
# products = list(input().split())
# bakery = {}
#
# key_list = []
# value_list = []
#
#
# for index in range(len(products)):
#     if index % 2 != 0:
#         value = int(products[index])
#         value_list.append(value)
#     else:
#         key = products[index]
#         key_list.append(key)
#
# for keys in key_list:
#     for values in value_list:
#         bakery[keys] = values
#         value_list.remove(values)
#         break
#
# print(bakery)


# ------------------------------------- Another Solution -----------------------------
#
# products = input().split()
# bakery = {}
#
# for index in range(0, len(products), 2):
#     key = products[index]
#     value = products[index + 1]
#     bakery[key] = int(value)
#
# print(bakery)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a single line containing some food (keys) and quantities (values). 
# They will be separated by a single space (the first element is the key, the second – the value, and so on). 
# Create a dictionary with all the keys and values and print it on the console.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                Output
# bread 10 butter 4 sugar 9 jam 12	    {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
# ---------------------------------------------------------------------------------------
# eggs 3 sugar 7 salt 1 butter 3	    {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}
