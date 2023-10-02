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


# ------------------------------------- Problem to resolve ------------------------------
#
# Create a class Inventory. The __init__ method should accept only the __capacity: int (private attribute)
# of the inventory. You can read more about private attributes here. Each inventory should also have an
# attribute called items - empty list, where all the items will be stored. The class should also have 3
# methods:
#       * add_item(item: str) - adds the item in the inventory if there is space for it. Otherwise, returns
#           "not enough room in the inventory"
#       * get_capacity() - returns the value of __capacity
#       * __repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}".
#           The items should be separated by ", "
#
# -------------------------------------- Example inputs ----------------------------------
# Test Code
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
# ----------------
# Output
# not enough room in the inventory
# 2
# Items: potion, sword.
# Capacity left: 0
