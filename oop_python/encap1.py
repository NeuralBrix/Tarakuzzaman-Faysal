class house:
    designer = "Dr. Muhammad Yunus"  #class attribute

    def __init__(self, owner): #constructor
        self.owner = owner
        self.__balance = 0 #private attribute

    def who_designer(self):
        print(f"The designer of the house is {house.designer}")

    def name(self):
        print(f"This will be the house for poor people")

owner1 = house("Faysal")
owner2 = house("Muhammad")

owner1.who_designer()
owner1.name()