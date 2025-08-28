class fighter:
    def fight(self):
        print("________________________Fighting for the legacy_______________________\n")
class mma(fighter):
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization
    def mma_fighter(self):
        print(f"{self.name} is a MMA fighter and he fought in {self.organization}")
        print(f"{self.name}'s most famous fight was 'UFC229' with Conor McGregor")
    def division(self, weight_class):
        self.weight_class = weight_class
        print(f"{self.name}'s weight class was {self.weight_class} Devision\n")    

class boxing(fighter):
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization
    def boxing_fighter(self):
        print(f"{self.name} is the Greatest Boxer Of All Time and he fought in {self.organization}") 
        print(f"{self.name}'s most famous boxing event is 'Rumble in the Jungle' with Jeorge Foreman 1974")  
    def division(self, weight_class):
        self.weight_class = weight_class
        print(f"{self.name}'s weight class was {self.weight_class} Devision")       

fighter1 = mma("khabib", "UFC")
fighter1.fight()
fighter1.mma_fighter()
fighter1.division("Lightweight")   

fighter2 = boxing("Mohammad Ali", "WBA")
fighter2.fight()
fighter2.boxing_fighter()
fighter2.division("Heavyweight")