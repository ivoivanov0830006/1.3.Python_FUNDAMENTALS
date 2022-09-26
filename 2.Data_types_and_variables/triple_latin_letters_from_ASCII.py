letters = int(input())
start = 97
end = start + letters

for i in range(start, end):
    for j in range(start, end):
        for k in range(start, end):
            print(f"{chr(i)}{chr(j)}{chr(k)}")
            

# --------------------------- Problem to resolve ----------------------------

# Write a program to read an integer N and print all triples of the first N small
# Latin letters, ordered alphabetically:
# Input	            Output
# 3	                aaa
#                   aab
#                   aac
#                   aba
#                   abb
#                   abc
#                   aca
#                   acb
#                   acc
#                   baa
#                   bab
#                   bac
#                   bba
#                   bbb
#                   bbc
#                   bca
#                   bcb
#                   bcc
#                   caa
#                   cab
#                   cac
#                   cba
#                   cbb
#                   cbc
#                   cca
#                   ccb
#                   ccc
# --------------------------------------
# 2	                aaa
#                   aab
#                   aba
#                   abb
#                   baa
#                   bab
#                   bba
#                   bbb
