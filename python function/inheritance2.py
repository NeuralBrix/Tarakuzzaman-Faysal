class fighters:
    def fight(self):
        print("________________________Fighting for the legacy_______________________\n")
class all_fighter(fighters):
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization
    def fighter(self):
        if self.organization == "UFC":
            print(f"{self.name} is a MMA fighter and he fought in {self.organization}")
            print(f"{self.name}'s most famous fight was 'UFC229' with Conor McGregor")
            
        elif self.organization == "WBA":
            print(f"{self.name} is the Greatest Boxer Of All Time and he fought in {self.organization}") 
            print(f"{self.name}'s most famous boxing event is 'Rumble in the Jungle' with Jeorge Foreman 1974")      
        
    def division(self, weight_class):
        self.weight_class = weight_class
        if self.organization == "UFC":
            print(f"{self.name}'s weight class was {self.weight_class} Devision\n") 
        elif self.organization == "WBA":
            print(f"{self.name}'s weight class was {self.weight_class} Division\n")     

fighter1 = all_fighter("khabib", "UFC")
fighter1.fight()
fighter1.fighter()
fighter1.division("Lightweight")   

fighter2 = all_fighter("Mohammad Ali", "WBA")
fighter2.fight()
fighter2.fighter()
fighter2.division("Heavyweight")        