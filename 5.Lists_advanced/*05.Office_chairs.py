total_rooms = int(input())

free_chairs = 0

for room in range(1, total_rooms + 1):
    information = input().split()
    chairs_number = len(information[0])
    people_number = int(information[1])
    diff = chairs_number - people_number
    if chairs_number < people_number:
        free_chairs -= abs(diff)
        print(f"{abs(diff)} more chairs needed in room {room}")
    else:
        free_chairs += diff
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")


# ------------------------------------- Another Solution -----------------------------
#
# def check_the_rooms(rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#     for room in range(1, rooms + 1):
#         free_chairs, visitors = input().split()
#         diff = len(free_chairs) - int(visitors)
#         if diff >= 0:
#             total_free_chairs += diff
#         else:
#             total_needed_chairs += abs(diff)
#             print(f"abs{diff} more chairs needed in room {room}")
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")


# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line, you will be given an integer n representing the number of rooms in
# the business center. On the following n lines for each room, you will receive information
# about the chairs in the room and the number of visitors. Each chair will be presented with
# the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# If there are not enough chairs in a specific room, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# Otherwise, print: "Game On, {total_free_chairs} free chairs left".
# Input	                        Output
# 4                             Game On, 4 free chairs left
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3
# ------------------------------------------------------------
# 3                             1 more chairs needed in room 2
# XXXXXXX 5                     2 more chairs needed in room 3
# XXXX 5
# XXXXXX 8
