number = int(input())
for i in range(1, number + 1):
    print(i * "*")
for j in range(number - 1, -1, -1):
    print(j * "*")
    
# --------------------------- Problem to resolve ----------------------------
#
# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
