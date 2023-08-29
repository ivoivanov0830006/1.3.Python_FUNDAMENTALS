number_line = int(input())
positives = []
negatives = []

for _ in range(number_line):
    current_number = int(input())

    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

# --------------------------- Problem to resolve -----------------------------
#
# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
#   ⦁	One with all the positives (including 0) args
#   ⦁	One with all the negatives args
# Finally, print the following message:
#   "Count of positives: {count_positives}
#   Sum of negatives: {sum_of_negatives}"
# Input	                        Output
# 5                             [10, 3, 2]
# 10                            [-15, -4]
# 3                             Count of positives: 3
# 2                             Sum of negatives: -19
# -15
# -4
#
#
# 
# 6
# 11
# 2
# 35
# 599
# 31
# 20	[11, 2, 35, 599, 31, 20]
# []
# Count of positives: 6
# Sum of negatives: 0
