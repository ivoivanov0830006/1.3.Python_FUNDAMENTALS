version = [int(number) for number in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print(".".join(str(number) for number in version))


# ------------------------------------- Another Solution -----------------------------
#
# version = input().split(".")
#
# current_version = int(version[0] + version[1] + version[2]) + 1
# next_version_num = str(current_version)
#
# print(".".join(next_version_num))


# ------------------------------------- Problem to resolve ------------------------------
#
# You will be given a string representing the version of your software in the format:
# "{n1}.{n2}.{n3}". Your task is to print the next version. For example, if the current version
# is "1.3.4", the next version will be "1.3.5".
# The only rule is that the args cannot be greater than 9. If it happens, set the current number
# to 0 and increase the previous number. For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.
# Input	                Output
# 1.2.3	                1.2.4
# 1.3.9	                1.4.0
# 3.9.9	                4.0.0

