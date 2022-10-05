def grades(current_grade):
    if 2 <= current_grade <= 2.99:
        return "Fail"
    elif 3 <= current_grade <= 3.49:
        return "Poor"
    elif 3.5 <= current_grade <= 4.49:
        return "Good"
    elif 4.5 <= current_grade <= 5.49:
        return "Very Good"
    elif 5.5 <= current_grade <= 6:
        return "Excellent"


current_grade = float(input())
print(grades(current_grade))

# ------------------------------------- Problem to resolve ------------------------------
#
# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# ⦁	2.00 – 2.99 - "Fail"
# ⦁	3.00 – 3.49 - "Poor"
# ⦁	3.50 – 4.49 - "Good"
# ⦁	4.50 – 5.49 - "Very Good"
# ⦁	5.50 – 6.00 - "Excellent"
# Input         	Output
# 3.33	            Poor
# 4.50	            Very Good
# 2.99	            Fail
