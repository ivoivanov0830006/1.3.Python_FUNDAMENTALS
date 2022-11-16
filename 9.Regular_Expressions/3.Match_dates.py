import re

data = input()
pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
dates = re.finditer(pattern, data)

for date in dates:
    current_object = date.group()
    day = current_object[0:2]
    month = current_object[3:6]
    year = current_object[-4:]

    print(f"Day: {day}, Month: {month}, Year: {year}")
    
    
# ------------------------------------- Another Solution -----------------------------
#
# import re
#
# data = input()
# pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
# dates = re.finditer(pattern, data)
#
# for date in dates:
#     group = date.groupdict()
#     print(f"Day: {group['day']}, Month: {group['month']}, Year: {group['year']}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.
# Every valid date has the following characteristics:
# ⦁	It always starts with two digits, followed by a separator
# ⦁	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
# ⦁	After that, it has a separator and exactly 4 digits (for the year).
# ⦁	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
# ⦁	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT).
# Use a group back reference to check for this.
# You can follow the table below to help with composing your RegEx:
# -------------------------------------- Example inputs ----------------------------------
# Input
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
# Output
# Day: 13, Month: Jul, Year: 1928
# Day: 10, Month: Nov, Year: 1934
# Day: 25, Month: Dec, Year: 1937
