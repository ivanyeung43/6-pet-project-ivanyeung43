""" class Hero:
    def __init__(self, name, money,  inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
        
John = Hero("John", 10, ["Map"])
John.buy({"title:": "Chestplate", "def": 10, "price": 12})
print(John.__dict__) """

class Pet:
    def __init__(self, name, happiness, action):
        self.name = name
        self.__happiness = happiness
        self.action = ""
    def play(self, action):
        self.__happiness += 10
        self.action = ""
        print(f"{self.name} is playing{self.action}")
    def show_status(self):
        print(f"{self.name} has {self.__happiness}")

Ruffs = Pet("Ruffs", 1, "")
Ruffs.play("Catch")
print(Ruffs.__dict__)