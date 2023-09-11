def shell(number):
    result = 2 * (number ** 2)
    return result


number_of_electrons = int(input())
electron_list = []
num = 0

while True:
    num += 1
    electron = shell(num)
    if number_of_electrons < shell(num):
        electron_list.append(number_of_electrons)
        break
    else:
        number_of_electrons -= electron
        electron_list.append(electron)

print(electron_list)


# ------------------------------------- Another Solution -----------------------------
#
# number_of_electrons = int(input())
# electron_list = []
# num = 1
# while number_of_electrons > 0:
#     current_electron = 2 * num ** 2
#     num += 1
#     if number_of_electrons - current_electron >= 0:
#         number_of_electrons -= current_electron
#     else:
#         current_electron = number_of_electrons
#         number_of_electrons = 0
#     electron_list.append(current_electron)
#
# print(electron_list)


# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a single integer - the number of electrons. Your task is to fill shells until
# there are no more electrons left. The rules for electron distribution are as follows:
# The maximum number of electrons in a shell can be 2n2, where n is the position of a shell
# (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# You should start filling the shells from the first one at the first position.
# If the electrons are enough to fill the first shell, the left unoccupied electrons
# should fill the following shell and so on.
# In the end, print a list with the filled shells.
# Input	                Output
# 10	                [2, 8]
# -----------------------------------------
# 44	                [2, 8, 18, 16]
