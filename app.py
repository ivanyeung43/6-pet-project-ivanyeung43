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
    def __init__(self, name, happiness, health, hunger, action):
        self.name = name
        self.__happiness = happiness
        self.__health = health
        self.__hunger = hunger
        self.action = action
        self.hunger = hunger
    def play(self, action):
        self.__happiness += 10
        self.action = action
        print(f"{self.name} is playing{self.action}")
    def feed(self, action):
        self.__hunger += 5
        self.action = action
        print(f"{self.name} is eating{self.action}")
    def care(self, action):
        self.__health += 5
        self.action = action
        print(f"{self.name} is being taken care of")
    def show_status(self):
        print(f"{self.name} has {self.__happiness} happiness, {self.__health} health points, and {self.__hunger} points")


def play(pet_name):
    pet_name = Pet(pet_name, 5, 5, 10, "")
    while int(action_taken)!= 5:
        action_taken = input("What would you like to do? Press 1 to feed, Press 2 to care, Press 3 to play and Press 4 to show status(Type 5 to stop the game)")
        if int(action_taken) == 5:
            break
        elif int(action_taken) == 1:
            pet_name.feed(" food")
        elif int(action_taken) == 2:
            pet_name.care(" bath")
        elif int(action_taken) == 3:
            pet_name.play(" fetch")
        elif int(action_taken) == 4:
            pet_name.show_status()
    pet_name.show_status()
    print("Game has ended.")

play(input("What would you like to name your pet?"))

