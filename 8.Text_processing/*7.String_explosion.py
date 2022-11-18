some_text = input()
new_text = ""
strength = 0

for index in range(len(some_text)):
    if strength > 0 and some_text[index] != ">":
        strength -= 1
    elif some_text[index] == ">":
        new_text += some_text[index]
        strength += int(some_text[index + 1])
    else:
        new_text += some_text[index]

print(new_text)


# ------------------------------------- Another Solution -----------------------------
#
# explosion_list = input().split(">")
#
# new_list = [explosion_list[0]]
# previous_count = 0
#
# for explosion in explosion_list:
#     count = 0
#     if explosion[0].isdigit():
#         power = int(explosion[0]) + previous_count
#         new_explosion = explosion[power:]
#         new_list.append(new_explosion)
#         previous_count = 0
#         if power > len(explosion):
#             count += power - len(explosion)
#             previous_count = count
#
# print(">".join(new_list))
