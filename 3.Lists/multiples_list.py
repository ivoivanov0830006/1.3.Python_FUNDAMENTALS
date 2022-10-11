factor = int(input())
count = int(input())
start = factor
end = factor * count

new_list = []

for number in range(start, end + 1):
    if number % factor == 0:
        new_list.append(number)
print(new_list)

