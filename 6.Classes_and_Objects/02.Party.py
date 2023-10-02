class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()
    if command == "End":
        break
    name = command
    party.people.append(name)

total_people = len(party.people)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people}")
