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
