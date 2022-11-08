countries = input().split(", ")
capitals = input().split(", ")

final_result = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in final_result.items():
    print(f"{country} -> {capital}")
    

# ------------------------------------- Another Solution -----------------------------
#
# countries = input().split(", ")
# capitals = input().split(", ")
#
# final_result = dict(zip(countries, capitals))
#
# for country, capital in final_result.items():
#     print(f"{country} -> {capital}")
#
#
# ------------------------------------- Problem to resolve ------------------------------
#
# Using a dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line (again
# separated by comma and space ", "). Print each country with their capital on a separate line in the
# following format: "{country} -> {capital}".
# -------------------------------------- Example inputs ----------------------------------
# Input	                                    Output
# Bulgaria, Romania, Germany, England       Bulgaria -> Sofia
# Sofia, Bucharest, Berlin, London	        Romania -> Bucharest
#                                           Germany -> Berlin
#                                           England -> London
# --------------------------------------------------------------
# Bulgaria, Germany, France                 Bulgaria -> Varna
# Varna, Frankfurt, Paris	                Germany -> Frankfurt
#                                           France -> Paris
