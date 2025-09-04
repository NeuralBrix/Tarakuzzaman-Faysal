class house:
    designer = "Dr. Muhammad Yunus"  #class attribute

    def __init__(self, owner): #constructor
        self.owner = owner
        self.__only_men = 0 #private attribute

    def who_designer(self):
        print(f"The designer of the house is {house.designer}")

    def name(self):
        print(f"This will be the house for poor people")

    def details(self):
        print(self.__only_men) 

    def set_condition(self, who_takes): #setter
        if isinstance(who_takes, str):
            self.__only_men = who_takes
        else:
            print("Only string value is allowed")

    def get_details(self): #getter
            print(self.__only_men)

    def __private_method(self): #private method
        print("This is a private method")

owner1 = house("Faysal")
owner2 = house("Muhammad")

owner1.set_condition("This houe is for all")
#owner1.details()
owner1.get_details()
#print(owner1.__dict__)

owner1._house__private_method() #can access private method
#print(_house.__private_method())
owner1.__private_method() #can not access