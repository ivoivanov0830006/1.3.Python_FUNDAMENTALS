path = input().split(f'{chr(92)}')
# path = input().split("\\")
searched_criteria = path[-1].split(".")
file_name = searched_criteria[0]
extension = searched_criteria[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")


# ------------------------------------- Problem to resolve ------------------------------
#
# Write a program that reads the path to a file and subtracts the file name and its extension.
# -------------------------------------- Example inputs ----------------------------------
# Input	                                                Output
# C:\Internal\training-internal\Template.pptx	        File name: Template
#                                                       File extension: pptx
# ---------------------------------------------------------------------------
# C:\Projects\Data-Structures\LinkedList.cs	            File name: LinkedList
#                                                       File extension: cs
