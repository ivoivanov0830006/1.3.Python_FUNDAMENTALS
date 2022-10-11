numbers = input()
negative_numbers_list = []

numbers_list = list(numbers.split(" "))

for string in numbers_list:
    negative_number = -int(string)
    negative_numbers_list.append(negative_number)
