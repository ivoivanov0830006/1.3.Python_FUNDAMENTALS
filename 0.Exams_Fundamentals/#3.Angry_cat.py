price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
items_type = input()

total_left_sum = 0
total_right_sum = 0

if items_type == "cheap":
    total_left_sum = sum([price_ratings[idx] for idx in range(entry_point)
                         if price_ratings[idx] < price_ratings[entry_point]])
    total_right_sum = sum([price_ratings[idx] for idx in range(entry_point + 1, len(price_ratings))
                          if price_ratings[idx] < price_ratings[entry_point]])

elif items_type == "expensive":
    total_left_sum = sum([price_ratings[idx] for idx in range(entry_point)
                         if price_ratings[idx] >= price_ratings[entry_point]])
    total_right_sum = sum([price_ratings[idx] for idx in range(entry_point + 1, len(price_ratings))
                          if price_ratings[idx] >= price_ratings[entry_point]])

if total_right_sum <= total_left_sum:
    print(f"Left - {total_left_sum}")
else:
    print(f"Right - {total_right_sum}")

    
# ------------------------------------- Another Solution -----------------------------
#
# price_ratings = list(map(int, input().split(", ")))
# entry_point = int(input())
# items_type = input()
#
# left_part = price_ratings[:entry_point]
# right_part = price_ratings[entry_point + 1::]
#
# total_sum_left = 0
# total_sum_right = 0
#
#
# if items_type == "cheap":
#     for price in left_part:
#         if price < price_ratings[entry_point]:
#             total_sum_left += price
#
#     for price in right_part:
#         if price < price_ratings[entry_point]:
#             total_sum_right += price
#
# elif items_type == "expensive":
#     for price in left_part:
#         if price >= price_ratings[entry_point]:
#             total_sum_left += price
#
#     for price in right_part:
#         if price >= price_ratings[entry_point]:
#             total_sum_right += price
#
# if total_sum_right <= total_sum_left:
#     print(f"Left - {total_sum_left}")
# else:
#     print(f"Right - {total_sum_right}")


# ------------------------------------- Problem to resolve ------------------------------
#
# A cat is breaking various household items. Each item has a price rating, a number that describes
# how valuable that item is for John's owner. You will be given an entry point from which John
# will break the items to his left and then to his right. John will never break the item at his
# entry point. You must calculate the damage to both his left and right, then print only the
# higher(bigger) damage to the household. If both sums are equal, print the left one.
# Input/Constrains
#       * On the first line, you will receive the price ratings, separated by(", "). Each element
# will be an integer in the range[-2^31...2^31].
#       * On the second line, you will receive the entry point, which will always be between the
# second and the penultimate element in the array.
#       * On the third line, you will receive the type of items that the cat wants to break, which
# will be one of the following:
#            - "cheap" - items that have a lower price rating than the entry point item
#            - "expensive" - items that have the same price rating, or higher price rating than
#           the entry point item.
# Output
#       * The possible output is: - "{position} - {sum of price ratings}"
#       * Positions can be "Right" or "Left"
# Input	                                        Output
# 1, 5, 1                                       Left - 1
# 1
# cheap
# --------------------------------------------------------
# 5, 10, 12, 5, 4, 20                           Right - 4
# 3
# cheap
# --------------------------------------------------------
# -2, 2, 1, 5, 9, 3, 2, -2, 1, -1, -3, 3        Left - 20
# 7
# expensive
