class house:
    designer = "Dr. Muhammad Yunus"  #class attribute

    def __init__(self, owner): #constructor
        self.owner = owner
        self.__balance = 0 #private attribute

    def who_designer(self):
        print(f"The designer of the house is {house.designer}")

    def name(self):
        print(f"This will be the house for poor people")

    def details(self):
        print(self.__balance)    

owner1 = house("Faysal")
owner2 = house("Muhammad")

owner1.who_designer()
owner1.name()

owner1.__balance = 1000
owner2.__balance = 2000

print(owner1.__dict__)
print(owner1.__balance)
print(owner2.__balance)
# print(owner1.balance)
# print(owner2.balance)

owner1.details()