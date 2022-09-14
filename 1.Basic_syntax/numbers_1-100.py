number = float(input())
is_in_range = False

while not is_in_range:
    if 1 <= number <= 100:
        is_in_range = True
        break
    number = float(input())
if is_in_range:
    print(f"The number {number} is between 1 and 100")


# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, the program should stop
# reading and should print "The number {number} is between 1 and 100".
# Input	                    Output
# -3
# 0.9
# 44	                    The number 44.0 is between 1 and 100
# ----------------------------------------------------------------------------------
# 0.5
# 90
# -4
# 101	                    The number 90.0 is between 1 and 100
