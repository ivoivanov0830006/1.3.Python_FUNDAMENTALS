numbers = list(map(int, input().split(" ")))
factor = int(input())
factored_numbers = list(map(lambda x: x * factor, numbers))

score = 0
average_happiness = 0

for employee in factored_numbers:
    average_happiness = sum(factored_numbers) / len(factored_numbers)
    if employee >= average_happiness:
        score += 1

if score >= average_happiness:
    print(f"Score: {score}/{len(factored_numbers)}. Employees are happy!")
else:
    print(f"Score: {score}/{len(factored_numbers)}. Employees are not happy!")


# ------------------------------------- Another Solution -----------------------------
#
# employee_happiness = list(map(int, input().split()))
# factor = int(input())
# updated_list = []
#
# for employee in employee_happiness:
#     employee *= factor
#     updated_list.append(employee)
#
# total_count = len(updated_list)
# average_happiness = sum(updated_list) / len(updated_list)
#
# filtered_employees = list(filter(lambda happiness: happiness > average_happiness, updated_list))
#
# happy_count = len(filtered_employees)
#
# if happy_count >= total_count / 2:
#     print(f"Score: {happy_count}/{total_count}. Employees are happy!")
# else:
#     print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive two lines of input:
#   ⦁	a list of employees' happiness as a string of args separated by a single space
#   ⦁	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
#   ⦁	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
#   ⦁	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
# Input	                    Output
# 1 2 3 4 2 1               Score: 2/6. Employees are not happy!
# 3
# ------------------------------------------------------------------
# 2 3 2 1 3 3               Score: 3/6. Employees are happy!
# 4
