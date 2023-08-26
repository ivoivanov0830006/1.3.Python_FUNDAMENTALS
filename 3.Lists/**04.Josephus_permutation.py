initial_list = list(map(int, input().split()))
given_index = int(input())

new_list = []
current_index = 0
counter = 0

while len(initial_list) > 0:
    counter += 1
    if counter % given_index == 0:
        new_list.append(initial_list[current_index])
        initial_list.pop(current_index)
    else:
        current_index += 1
    if current_index >= len(initial_list):
        current_index = 0
print(str(new_list).replace(" ", ""))
