class Fighter:
    def __init__(self, name):
        self.name = name

    def add_record(self, win, loss=None, draw=None):
        self.win = win
        self.loss = loss
        self.draw = draw

        if self.draw is not None:
            print(f"{self.name} has a professional record of ({self.win}-{self.loss}-{self.draw})")
        elif self.loss and self.draw is None:
            print(f"{self.name} has a professional record of ({self.win}-{self.loss})")
        else: 
            print(f"{self.name} has a professional record of ({self.win})")

fighter1 = Fighter("Conor McGregor")

fighter1.add_record(22, 6, 0)
fighter1.add_record(22, 6)
fighter1.add_record(22)
print("_________________________________________________\n")
fighter2 = Fighter("Khabib Nurmagomedov")

fighter2.add_record(29, 0, 0)
fighter2.add_record(29, 0)
fighter2.add_record(29)