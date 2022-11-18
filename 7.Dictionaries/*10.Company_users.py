company = {}

while True:
    command = input()
    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")
    if company_name not in company.keys():
        company[company_name] = []
    if employee_id not in company[company_name]:
        company[company_name].append(employee_id)

for key, value in company.items():
    print(f"{key}")
    for values in company[key]:
        print(f"-- {values}")

        
# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the
# same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# The input always will be valid.
# -------------------------------------- Example inputs ----------------------------------
# Input	                            Output
# SoftUni -> AA12345                SoftUni
# SoftUni -> BB12345                -- AA12345
# Microsoft -> CC12345              -- BB12345
# HP -> BB12345                     Microsoft
# End	                            -- CC12345
#                                   HP
#                                   -- BB12345
# ---------------------------------------------
# SoftUni -> AA12345                SoftUni
# SoftUni -> CC12344                -- AA12345
# Lenovo -> XX23456                 -- CC12344
# SoftUni -> AA12345                Lenovo
# Movement -> DD11111               -- XX23456
# End	                            Movement
#                                   -- DD11111
