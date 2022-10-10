def min_num(my_numbers_list):
    min_number = min(my_numbers_list)
    return min_number


def max_num(my_numbers_list):
    max_number = max(my_numbers_list)
    return max_number


def sum_all_num(my_numbers_list):
    result = sum(my_numbers_list)
    return result


numbers_list = list(map(int, input().split(" ")))

minimum_number = min_num(numbers_list)
maximum_number = max_num(numbers_list)
total_sum = sum_all_num(numbers_list)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {total_sum}")
