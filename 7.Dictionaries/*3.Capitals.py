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

