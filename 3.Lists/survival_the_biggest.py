initial_list = input().split()
remove = int(input())

final_list = []

for string in initial_list:
    number = int(string)
    final_list.append(number)

for element in range(remove):
    final_list.remove(min(final_list))

output = [str(x) for x in final_list]

print(", ".join(output))

# --------------------------- Problem to resolve -----------------------------
#
# Write a program that receives a list of integer numbers (separated by a single space) and a number n. 
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones,
# and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".
# Input	                            Output
# 10 9 8 7 6 5                      10, 9, 8
# 3	
# ----------------------------------------------------
# 1 10 2 9 3 8                      10, 9, 3, 8
# 2	
