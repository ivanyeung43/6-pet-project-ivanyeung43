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
    def __init__(self, name,happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, fetch, catch):


dog = Pet("dog", 0)
dog.play
print(dog.__dict__)
