class Fighter:
    def __init__(self, name):
        self.name = name
    
    def fight(self):
        print(f"{self.name} can fight!")

    def organization(self, org):
        self.org = org
        print(f"{self.name} fight in the {self.org}")
    
fighter1 = Fighter("Dustin Poirier")
fighter1.fight()
fighter1.organization("UFC")
#Polymorphisom
class MMA(Fighter):
    def __init__(self, name, nickname):
        super().__init__(name)
        self.nickname = nickname
        self.org = None

    def fight(self): #overriding fight method
        print(f"{self.name} can fight. his nickname is {self.nickname}.")    

    def organization(self, org): #overriding organization method
        super().organization(org)
        print(f"{self.name} fight in the {self.org}")

def get_info(information):
    information.fight()
    information.organization("Boxing")

fighter1 = Fighter("Conor McGregor")
fighter2 = MMA("Khabib Nurmagomedov", "The Eagle")

get_info(fighter1)
get_info(fighter2)

