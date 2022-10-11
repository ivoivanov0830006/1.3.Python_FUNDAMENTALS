factor = int(input())
count = int(input())
start = factor
end = factor * count

new_list = []

for number in range(start, end + 1):
    if number % factor == 0:
        new_list.append(number)
print(new_list)

# --------------------------- Another solution ----------------------------
#
# factor = int(input())
# count = int(input())
# new_list = []
# number = 0
#
# for _ in range(1, count + 1):
#     number += factor
#     new_list.append(int(number))
#
# print(new_list)
