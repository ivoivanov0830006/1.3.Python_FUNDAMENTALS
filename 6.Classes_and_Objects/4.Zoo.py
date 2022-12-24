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
