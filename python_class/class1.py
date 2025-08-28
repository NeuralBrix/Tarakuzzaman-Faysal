class human:
    def __init__(self, name, profession, fame):
        self.name = name
        self.profession = profession
        self.fame = fame
    def work(self):
        if self.profession == "Footballer":
            print(f"{self.name} is the GOAT of Football")
        elif self.profession == "UFC":
            print(f"{self.name} is one of the best fighters in MMA")
    def famous_for(self):
        if self.fame == "Undefeated":
            print(f"{self.name} is an Undefeated fighter, his record is (29-0)")  
        elif self.fame == "Best in Football":
            print(f"{self.name} wins the world cup, and he wins 8 ballon d'or")        

human1 = human("Khabib", "UFC", "Undefeated")
human1.work()
human1.famous_for()

human2 = human("Messi", "Footballer", "Best in Football")
human2.work()
human2.famous_for()
