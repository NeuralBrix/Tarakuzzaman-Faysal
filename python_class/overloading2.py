from multipledispatch import dispatch

class Fighter:
    def __init__(self, name):
        self.name = name
    @dispatch(int, int, int)
    def add_record(self, win, loss, draw):
        self.win = win
        self.loss = loss
        self.draw = draw
        print(f"{self.name} has a professional record of ({self.win}-{self.loss}-{self.draw})")
    @dispatch(int, int)
    def add_record(self, win, loss):
        self.win = win
        self.loss = loss
        print(f"{self.name} has a professional record of ({self.win}-{self.loss})")
    @dispatch(int)
    def add_record(self, win):
        self.win = win
        print(f"{self.name} has a professional record of ({self.win})")

fighter1 = Fighter("Conor McGregor")
fighter1.add_record(22, 6, 0)
fighter1.add_record(22, 6)
fighter1.add_record(22)
print("___________________________________________________________\n")

fighter2 = Fighter("Khabib Nurmagomedov")
fighter2.add_record(29, 0, 0)
fighter2.add_record(29, 0)
fighter2.add_record(29)