def sum_even(num):
    even_list = []
    number_string = [int(x) for x in str(num)]
    for index in number_string:
        if index % 2 == 0:
            even_list.append(index)
    total_sum_even = sum(even_list)
    return total_sum_even


def sum_odd(num):
    odd_list = []
    number_string = [int(x) for x in str(num)]
    for index in number_string:
        if index % 2 != 0:
            odd_list.append(index)
    total_sum_odd = sum(odd_list)
    return total_sum_odd


number_input = int(input())

sum_of_odd_digits = sum_odd(number_input)
sum_of_even_digits = sum_even(number_input)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

# ------------------------------------- Another Solution -----------------------------
#
# def even_sum_and_odd_sum(number):
#     sum_odd = 0
#     sum_even = 0
#     for digit in number:
#         if int(digit) % 2 == 0:
#             sum_even += int(digit)
#         else:
#             sum_odd += int(digit)
#     return sum_even, sum_odd
#
#
# number_string = input()
# sum_of_odd_digits, sum_of_even_digits = even_sum_and_odd_sum(number_string)
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
#
