money_list = input().split(", ")
count_beggars = int(input())

split_money_list = []
money_as_digit = []

starting_index = 0

for element in money_list:
    money_as_digit.append(int(element))

while starting_index < count_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_as_digit), count_beggars):
        sum_for_current_beggar += money_as_digit[current_index]
    split_money_list.append(sum_for_current_beggar)
    starting_index += 1
print(split_money_list)

# --------------------------- Problem to resolve -----------------------------
#
# You will receive 2 lines of input. On the first line, you will receive a single string of
# integers, separated by a comma and a space ", ". On the second line, you will receive a count
# of beggars. Your job is to print a list with the sum of what each beggar brings home, assuming
# hey all take regular turns, from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one
# takes [1, 3, 5], the second one collects [2, 4]. The same list with 3 beggars would produce a
# better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length
# of the list is not necessarily a multiple of n. The list length could be even shorter - i.e., the
# last beggars will take nothing (0).
# Input	                            Output
# 1, 2, 3, 4, 5                     [9, 6]
# 2
# ----------------------------------------------------------
# 3, 4, 5, 1, 29, 4                 [3, 4, 5, 1, 29, 4]
# 6
# -----------------------------------------------------------
# 100, 94, 24, 99                   [100, 94, 24, 99, 0]
# 5
