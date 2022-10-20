sequence = list(map(int, input().split()))
new_list = [num for num in sequence if num > (sum(sequence) / len(sequence))]

