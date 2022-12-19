for string in range(int(input())):
    is_pure = True
    text = input()
    for char in range(len(text)):
        if text[char] == "," or text[char] == "." or text[char] == "_":
            is_pure = False
            break
        else:
            continue
    if is_pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
        
        
# --------------------------- Another solution ----------------------------
#
# for string in range(int(input())):
#     text = input()
#     if "," in text or "." in text or "_" in text:
#         print(f"{text} is pure.")
#     else:
#         print(f"{text} is not pure!"
