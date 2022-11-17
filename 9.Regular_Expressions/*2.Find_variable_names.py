import re

text = input()
pattern = r"(?P<underscore>\b_{1})(?P<text>[a-zA-Z0-9]+\b)"

results = re.finditer(pattern, text)
valid_strings = []

for result in results:
    valid_strings.append(result[2])

print(",".join(valid_strings))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that finds all variable names in each string. A variable name starts with an
# underscore ("_") and contains only capital and non-capital letters and digits. Extract only their names
# without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                                            Output
# The _id and _age variables are both integers.	                    id,age
# ----------------------------------------------------------------------------------------
# Calculate the _area of the _perfectRectangle object.	            area,perfectRectangle
# ----------------------------------------------------------------------------------------
# __invalidVariable _evenMoreInvalidVariable_ _validVariable	    validVariable
