row_1 = list(map(int, input().split()))
row_2 = list(map(int, input().split()))
row_3 = list(map(int, input().split()))

column_1 = [row_1[0], row_2[0], row_3[0]]
column_2 = [row_1[1], row_2[1], row_3[1]]
column_3 = [row_1[2], row_2[2], row_3[2]]

diagonal_1 = [row_1[0], row_2[1], row_3[2]]
diagonal_2 = [row_1[2], row_2[1], row_3[0]]

# horizontals
if row_1.count(1) == 3 or row_2.count(1) == 3 or row_3.count(1) == 3:
    print("First player won")
elif row_1.count(2) == 3 or row_2.count(2) == 3 or row_3.count(2) == 3:
    print("Second player won")
# verticals
elif column_1.count(1) == 3 or column_2.count(1) == 3 or column_3.count(1) == 3:
    print("First player won")
elif column_1.count(2) == 3 or column_2.count(2) == 3 or column_3.count(2) == 3:
    print("Second player won")
# diagonals
elif diagonal_1.count(1) == 3 or diagonal_2.count(1) == 3:
    print("First player won")
elif diagonal_1.count(2) == 3 or diagonal_2.count(2) == 3:
    print("Second player won")

else:
    print("Draw!")
    

# ------------------------------------- Problem to resolve ------------------------------
#
# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a
# single space.
# Legend:
#   0 - empty space
#   1 - first player move
#   2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins,
# print "Second player won". Otherwise, print "Draw!".
#
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 2 0 1                       First player won
# 0 1 0
# 1 0 2
# -----------------------------------------------
# 0 1 0                       Second player won
# 2 2 2
# 1 0 0
# -----------------------------------------------
# 1 0 2                       Draw!
# 0 1 2
# 1 2 0
