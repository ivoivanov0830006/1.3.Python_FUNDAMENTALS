names = input().split(", ")
result = sorted(names, key=lambda item: (-len(item), item))
print(result)


#####################################################################################
# result = sorted(names, key=lambda item: (-len(item), item)) ...item:
# (parvo daljinata, posle azbuchen red)
# (- e po golqmata daljina)
# Item e neshto dinamichno ! to vzema imenata
# i gi proverqva
# ----------------------------------------------------------------------------------
# sorted vaji samo v situaciqta koqto polzvame, ako izvikame spisaka names otnovo
# to toi shte si bade otnovo nepodreden
# dokato sort nanasq traini promeni
#####################################################################################


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order. If 2 or more names have the same length,
# sort them in ascending order (alphabetically). Print the resulting list.
# Input	                                    Output
# Ali, Marry, Kim, Teddy, Monika, John      ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]
# ---------------------------------------------------------------------------------------------
# Lilly, Tim, Kate, Tom, Alex	            ['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']
