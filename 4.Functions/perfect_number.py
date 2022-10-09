def aliquot_sum(input_number):
    total_sum = 0
    for divisor in range(1, input_number):
        if input_number % divisor == 0:
            total_sum += divisor
    if total_sum == input_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

aliquot_sum(number)
