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
    

# ------------------------------------- Problem to resolve ------------------------------
#
# On the first line of the standard input, you will receive an integer n – the number of pieces you
# will initially have. On the next n lines, the pieces themselves will follow with their composer and key,
# separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop"
# command is given:
# "Add|{piece}|{composer}|{key}":
#       You need to add the given piece with the information about it to the other pieces and print:
#       "{piece} by {composer} in {key} added to the collection!"
#       If the piece is already in the collection, print:
#       "{piece} is already in the collection!"
# "Remove|{piece}":
#       If the piece is in the collection, remove it and print:
#       "Successfully removed {piece}!"
#       Otherwise, print:
#       "Invalid operation! {piece} does not exist in the collection."
# "ChangeKey|{piece}|{new key}":
#       If the piece is in the collection, change its key with the given one and print:
#       "Changed the key of {piece} to {new key}!"
#       Otherwise, print:
#       "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
#       "{Piece} -> Composer: {composer}, Key: {key}"
# -------------------------------------- Example inputs ----------------------------------
# Input
# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
#
# Output
# Sonata No.2 by Chopin in B Minor added to the collection!
# Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
# Fur Elise is already in the collection!
# Successfully removed Clair de Lune!
# Changed the key of Moonlight Sonata to C# Major!
# Fur Elise -> Composer: Beethoven, Key: A Minor
# Moonlight Sonata -> Composer: Beethoven, Key: C# Major
# Sonata No.2 -> Composer: Chopin, Key: B Minor
# Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor
# ------------------------------------------------------------------------------------------
# Input
# 4
# Eine kleine Nachtmusik|Mozart|G Major
# La Campanella|Liszt|G# Minor
# The Marriage of Figaro|Mozart|G Major
# Hungarian Dance No.5|Brahms|G Minor
# Add|Spring|Vivaldi|E Major
# Remove|The Marriage of Figaro
# Remove|Turkish March
# ChangeKey|Spring|C Major
# Add|Nocturne|Chopin|C# Minor
# Stop
#
# Output
# Spring by Vivaldi in E Major added to the collection!
# Successfully removed The Marriage of Figaro!
# Invalid operation! Turkish March does not exist in the collection.
# Changed the key of Spring to C Major!
# Nocturne by Chopin in C# Minor added to the collection!
# Eine kleine Nachtmusik -> Composer: Mozart, Key: G Major
# La Campanella -> Composer: Liszt, Key: G# Minor
# Hungarian Dance No.5 -> Composer: Brahms, Key: G Minor
# Spring -> Composer: Vivaldi, Key: C Major
# Nocturne -> Composer: Chopin, Key: C# Minor
