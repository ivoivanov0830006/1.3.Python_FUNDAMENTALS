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
# ------------------------------------- Another Solution -----------------------------
#
# def login(input_pass):
#     number_count = 0
#     validation = []
#     if len(input_pass) < 6 or len(input_pass) > 10:
#         validation.append("Password must be between 6 and 10 characters")
#     if not input_pass.isalnum():
#         validation.append("Password must consist only of letters and digits")
#     for char in input_pass:
#         if char.isdigit():
#             number_count += 1
#     if number_count < 2:
#         validation.append("Password must have at least 2 digits")
#     return validation
#
#
# password = input()
# password_is_not_valid = login(password)
# if len(password_is_not_valid) == 0:
#     print("Password is valid")
# else:
#     print("\n".join(password_is_not_valid))
#
# ------------------------------------- Problem to resolve ------------------------------
#
#   Write a function that checks if a given password is valid. Password validations are:
#       - It should be 6 - 10 (inclusive) characters long
#       - It should consist only of letters and digits
#       - It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
#       - "Password must be between 6 and 10 characters"
#       - "Password must consist only of letters and digits"
#       - "Password must have at least 2 digits"
# Input	            Output
# logIn	            Password must be between 6 and 10 characters
#                   Password must have at least 2 digits
# ---------------------------------------------------------------
# MyPass123	        Password is valid
# ---------------------------------------------------------------
# Pa$s$s	        Password must consist only of letters and digits
#                   Password must have at least 2 digits
