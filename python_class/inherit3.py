class Fighter:
    def __init__(self, name):
        self.name = name
    def fight(self):
        print(f"{self.name} can fight!")
    def info(self):
        print(f"{self.name} is an undefeated fighter.")

class MMA(Fighter):
    def __init__(self, name, fighter_name):
        super().__init__(name)
        self.fighter_name = fighter_name
    def fight(self):
        print(f"{self.name} is a MMA fighter. Nickname is {self.fighter_name}.")

fighter1 = MMA("Khabib", "The Eagle")
fighter1.fight()

fighter1.info()


