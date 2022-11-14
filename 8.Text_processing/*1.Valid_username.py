all_usernames = input().split(", ")
valid_username = []

for username in all_usernames:
    has_problem = False
    if 3 < len(username) <= 16:
        for symbol in username:
            if symbol.isalpha() or symbol.isdigit() or symbol == "_" or symbol == "-":
                continue
            else:
                has_problem = True
                break
        if has_problem:
            continue
        valid_username.append(username)
print("\n".join(valid_username))


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads usernames on a single line (separated by ", ") and prints all valid
# usernames on separate lines.
# A valid username:
#   * has length between 3 and 16 characters inclusive
#   * can contain only letters, numbers, hyphens, and underscores
#   * has no redundant symbols before, after, or in between
# -------------------------------------- Example inputs ----------------------------------
# Input         	                                        Output
# sh, too_long_username, !lleg@l ch@rs, jeffbutt	        jeffbutt
# -------------------------------------------------------------------
# Jeff, john45, ab, cd, peter-ivanov, @smith	            Jeff
#                                                           John45
#                                                           peter-ivanov
