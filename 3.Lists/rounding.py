input_list = input().split()

round_list = []

for string in input_list:
    number = float(string)
    round_list.append(round(number))
print(round_list)

# ------------------------------------- Another Solution -----------------------------
#
# result = list(map(lambda x: round(float(x)), input().split("")))
# print(result)


