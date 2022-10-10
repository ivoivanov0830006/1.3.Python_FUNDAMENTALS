def palindrome(num_list):
    for number in num_list:
        num_string = str(number)
        size = len(num_string)
        reversed_num = num_string[size::-1]
        if reversed_num == number:
            print("True")
        else:
            print("False")


numbers_list = list(input().split(", "))
palindrome(numbers_list)
