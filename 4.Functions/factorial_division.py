def factorial(number):
    for num in range(1, number):
        number *= num
    return number


def end_result(factorial_1, factorial_2):
    return f"{(factorial_1 / factorial_2):.2f}"


number_1 = int(input())
number_2 = int(input())

print(end_result(factorial(number_1), factorial(number_2)))
