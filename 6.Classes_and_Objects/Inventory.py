class Inventory:
    items = []

    def __init__(self, capacity: int):
        self.__capacity = capacity

    def add_item(self, item: str):
        if self.__capacity > 0:
            Inventory.items.append(item)
            self.__capacity -= 1
        return "not enough room in the inventory"

    def get_capacity(self):
        return len(Inventory.items)

    def __repr__(self):
        string_result = ", ".join(Inventory.items)
        return f"Items: {string_result}.\nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
