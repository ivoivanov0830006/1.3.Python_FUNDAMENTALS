path = input().split(f'{chr(92)}')
# path = input().split("\\")
searched_criteria = path[-1].split(".")
file_name = searched_criteria[0]
extension = searched_criteria[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
