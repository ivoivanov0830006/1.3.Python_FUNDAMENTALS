initial_gifts = input().split()
command = input()

while command != "No Money":
    input_items = command.split(" ")
    order_type = input_items[0]
    gift_type = input_items[1]
    if order_type == "OutOfStock":
        for item, n in enumerate(initial_gifts):
            if n == gift_type:
                initial_gifts[item] = "None"
    elif order_type == "Required":
        gift_index = int(input_items[2])
        if 0 <= gift_index < len(initial_gifts):
            initial_gifts[gift_index] = input_items[1]
    elif order_type == "JustInCase":
        initial_gifts[-1] = input_items[1]
    command = input()

while "None" in initial_gifts:
    initial_gifts.remove("None")
print(" ".join(initial_gifts))

# --------------------------- Another solution ----------------------------

# gifts_list = [x for x in input().split()]
# direction = input()
#
# while direction != 'No Money':
#     direction = direction.split()
#     event = direction[0]
#     gift = direction[1]
#     if event == 'OutOfStock':
#         for _ in range(gifts_list.count(gift)):
#             idx = gifts_list.index(gift)
#             gifts_list.insert(idx, 'None')
#             gifts_list.pop(idx + 1)
#     elif event == 'Required':
#         index = int(direction[2])
#         if 0 <= index < len(gifts_list):
#             gifts_list.insert(index, gift)
#             gifts_list.pop(index + 1)
#     elif event == 'JustInCase':
#         gifts_list.pop()
#         gifts_list.append(gift)
#     direction = input()
#
# for gift in gifts_list:
#     if gift != 'None':
#         print(gift, end=' ')

# --------------------------- Problem to resolve -----------------------------
#
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive
# the gifts you plan on buying on a single line, separated by space, in the following format:
#       - "{gift1} {gift2} {gift3} ... {gift n}"
#       Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#       - "OutOfStock {gift}"
#       Find the gifts with this name in your collection, if any, and change their values to "None".
#       - "Required {gift} {index}"
#       If the index is valid, replace the gift on the given index with the given gift.
#       - "JustInCase {gift}"
#       Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in
# the following format:
#       - "{gift1} {gift2} {gift3} … {gift n}"
# Input / Constraints
#   On the 1st line,  you will receive the names of the gifts, separated by a single space.
#   On the following lines, until the "No Money" direction is received, you will be receiving commands.
#   The input will always be valid.
# Output
#   Print the gifts in the format described above.
# Input	                                                        Output
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes    StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
