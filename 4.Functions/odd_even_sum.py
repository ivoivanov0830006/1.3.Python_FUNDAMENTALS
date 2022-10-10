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

