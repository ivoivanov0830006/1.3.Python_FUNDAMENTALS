sequence = list(map(int, input().split()))
new_list = [num for num in sequence if num > (sum(sequence) / len(sequence))]

if len(new_list) < 1:
    print("No")
new_list.sort(reverse=True)
print(*new_list[:5], sep=" ")
