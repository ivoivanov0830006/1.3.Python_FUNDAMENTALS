def average(total_sum, grades_count):
    return total_sum / grades_count


academy = {}
count = int(input())

for _ in range(count):

    name = input()
    grade = float(input())
    if name not in academy.keys():
        academy[name] = []
    academy[name].append(grade)

for key, value in academy.items():
    average_grade = average(sum(value),len(value))
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")
