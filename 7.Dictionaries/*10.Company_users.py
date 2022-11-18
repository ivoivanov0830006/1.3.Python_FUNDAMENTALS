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
