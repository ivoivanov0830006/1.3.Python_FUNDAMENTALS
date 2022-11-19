number_of_lines = int(input())

records = {}

for _ in range(number_of_lines):
    piece, composer, key = input().split("|")
    if piece not in records:
        records[piece] = []
    records[piece].append(composer)
    records[piece].append(key)

command = input()

while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]

    if action == "Add":
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if piece not in records.keys():
            records[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = current_command[1]
        if piece in records.keys():
            del records[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = current_command[1]
        new_key = current_command[2]
        if piece in records.keys():
            records[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for key, value in records.items():
    song_name = key
    song_composer = value[0]
    song_key = value[1]
    print(f"{song_name} -> Composer: {song_composer}, Key: {song_key}")
    
