def login(input_pass):
    number_count = 0
    is_valid = True
    for char in input_pass:
        symbol = ord(char)
        if 48 <= symbol <= 57:
            number_count += 1
        if symbol < 48 or 57 < symbol < 65 or 90 < symbol < 97 or symbol > 122:
            is_valid = False
            print("Password must consist only of letters and digits")
            break
    if 10 < len(input_pass) or len(input_pass) < 6:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if number_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


password = input()
login(password)

# ------------------------------------- Another Solution -----------------------------
#
# def login(input_pass):
#     number_count = 0
#     is_valid = True
#     if len(input_pass) < 6 or len(input_pass) > 10:
#         print("Password must be between 6 and 10 characters")
#         is_valid = False
#     if not input_pass.isalnum():
#         print("Password must consist only of letters and digits")
#         is_valid = False
#     for char in input_pass:
#         if char.isdigit():
#             number_count += 1
#     if number_count < 2:
#         print("Password must have at least 2 digits")
#         is_valid = False
#     return is_valid
#
#
# password = input()
# password_is_valid = login(password)
# if password_is_valid:
#     print("Password is valid")
#
