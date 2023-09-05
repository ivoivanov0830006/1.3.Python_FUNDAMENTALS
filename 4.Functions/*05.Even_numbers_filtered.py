def check_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers_list = list(map(int, input().split(" ")))
filtered_even_numbers = filter(check_numbers, numbers_list)
print(list(filtered_even_numbers))
