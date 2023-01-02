century = int(input())
year = century * 100
day = int(year * 365.2422)
hour = day * 24
minute = hour * 60

print(f"{century} centuries = {year} years = {day} days = {hour} hours = {minute} minutes")
