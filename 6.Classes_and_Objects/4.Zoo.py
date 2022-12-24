class Zoo:
    __animals = []

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals.append(self.name)

    def get_info(self, input_species):
        result = ""
        if input_species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {len(zoo.__animals)}"
        elif input_species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fish)}\nTotal animals: {len(zoo.__animals)}"
        elif input_species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {len(zoo.__animals)}"
        return result


input_zoo_name = input()
input_animal_count = int(input())

zoo = Zoo(input_zoo_name)

for _ in range(input_animal_count):
    current_species, current_name = input().split()
    zoo.add_animal(current_species, current_name)

criteria = input()

print(zoo.get_info(criteria))


# ------------------------------------- Problem to resolve ------------------------------
#
# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the
# animals in the zoo. The __init__ method should only receive the name of the zoo. There you should also
# create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
# ⦁	add_animal(species, name) - based on the species, adds the name to the corresponding list
# ⦁	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}
# Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
# On the following n lines you will receive animal info in the format: "{species} {name}". Add the animal
# to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species.
# At the end, print the info for that species and the total count of animals in the zoo.
# -------------------------------------- Example inputs ----------------------------------
# Input	                        Output
# Great Zoo                     Mammals in Great Zoo: lion, bear, tiger
# 5                             Total animals: 5
# mammal lion
# mammal bear
# fish salmon
# bird owl
# mammal tiger
# mammal
# --------------------------------------------------------------------------
# Blah                          Mammals in Blah: bear
# 1                             Total animals: 1
# mammal bear
# mammal
