total_numbers = int(input())

for _ in range(total_numbers):
    number = int(input())
    if number % 2 == 0:
        continue
    else:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

# --------------------------- Problem to resolve ----------------------------
#
# Write a program that receives a number n on the first line. On the following n lines, 7
# it receives different integer numbers. If the program receives an odd number,
# print "{num} is odd!" and end the program. Otherwise, if all numbers given are even,
# print "All numbers are even.".
# Input	                    Output
# 2
# 12
# 286	                    All numbers are even.
# ------------------------------------------------------------
# 5
# 2
# 9	                        9 is odd!
