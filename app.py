# Lesson 1
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

""" class Pet:
    def __init__(self, name, happiness, action):
        self.name = name
        self.__happiness = happiness
        self.action = action
    def play(self, action):
        self.__happiness += 10
        self.action = action
        print(f"{self.name} is playing{self.action}")
    def show_status(self):
        print(f"{self.name} has {self.__happiness} happiness.")

Ruffs = Pet("Ruffs", 1, "")
Ruffs.play(" fetch.")
Ruffs.show_status() """

# Pet Project

class Pet:
    def __init__(self, name, happiness, health, action, hunger):
        self.name = name
        self.__happiness = happiness
        self.__health = health
        self.action = action
        self.hunger = hunger
    def Naming(self, name):
        self.name = input(name)
        print(input("What would you like to name the pet"))

"" = Pet
