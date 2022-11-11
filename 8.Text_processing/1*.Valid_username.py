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
