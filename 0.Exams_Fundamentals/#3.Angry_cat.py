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
