def sum_numbers(a, b):
    result = a + b
    return result


def subtract(sum_num, c):
    result = sum_num - c
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

total = subtract((sum_numbers(num_1, num_2)), num_3)
print(total)

