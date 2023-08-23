numbers_list = list(map(int, input().split(", ")))
for num in numbers_list:
    if num == 0:
        numbers_list.append(0)
        numbers_list.remove(0)
print(numbers_list)


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting
# integer list.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 1, 0, 1, 2, 0, 1, 3	    [1, 1, 2, 1, 3, 0, 0]
# -------------------------------------------------
# 0, 5, 0, 4, 0, 0, 5	    [5, 4, 5, 0, 0, 0, 0]
#
