def exchange_func(my_number_list, index: int):
    for item in my_number_list[:index + 1]:
        my_number_list.append(item)
        my_number_list.remove(item)
    return my_number_list


def max_func(my_number_list, number_type: str):
    current_idx = 'No matches'
    max_number = 0
    if number_type == 'even':
        for index, number in enumerate(my_number_list):
            if number % 2 == 0:
                if number >= max_number:
                    max_number = number
                    current_idx = index
        return current_idx
    elif number_type == 'odd':
        for index, number in enumerate(my_number_list):
            if number % 2 != 0:
                if number >= max_number:
                    max_number = number
                    current_idx = index
        return current_idx


def min_func(my_number_list, number_type: str):
    current_idx = 'No matches'
    min_number = max(my_number_list)
    if number_type == 'even':
        for index, number in enumerate(my_number_list):
            if number % 2 == 0:
                if number <= min_number:
                    min_number = number
                    current_idx = index
        return current_idx
    elif number_type == 'odd':
        for index, number in enumerate(my_number_list):
            if number % 2 != 0:
                if number <= min_number:
                    min_number = number
                    current_idx = index
        return current_idx


def first_func(my_number_list, number_count: int, number_type: str):
    odd_list = []
    even_list = []
    for num in my_number_list:
        if num % 2 != 0:
            odd_list.append(num)
        elif num % 2 == 0:
            even_list.append(num)
    if number_type == "odd":
        return odd_list[0:number_count]
    elif number_type == "even":
        return even_list[0:number_count]


def last_func(my_number_list, number_count: int, number_type: str):
    odd_list = []
    even_list = []
    for num in my_number_list:
        if num % 2 != 0:
            odd_list.append(num)
        elif num % 2 == 0:
            even_list.append(num)
    if number_type == "odd":
        return odd_list[-number_count:]
    elif number_type == "even":
        return even_list[-number_count:]


input_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    current_command = command.split()
    current_action = current_command[0]
    if current_action == "exchange":
        current_index = int(current_command[1])
        if current_index >= len(input_list) or current_index < 0:
            print("Invalid index")
            continue
        input_list = exchange_func(input_list, current_index)
    elif current_action == "max":
        current_input = current_command[1]
        print(max_func(input_list, current_input))
    elif current_action == "min":
        current_input = current_command[1]
        print(min_func(input_list, current_input))
    elif current_action == "first":
        current_count = int(current_command[1])
        current_input = current_command[2]
        if current_count > len(input_list) or current_count < 0:
            print("Invalid count")
            continue
        print(first_func(input_list, current_count, current_input))
    elif current_action == "last":
        current_count = int(current_command[1])
        current_input = current_command[2]
        if current_count > len(input_list) or current_count < 0:
            print("Invalid count")
            continue
        print(last_func(input_list, current_count, current_input))

print(input_list)
