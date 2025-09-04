class fighters:
    def __init__(self):
        print("A new fighter has entered the arena!")
    def fighter(self, name):
        self.name = name
        return "They are fighters"
    def organization(self, org_name):
        print(f'{self.name} is fighting in {org_name}')
        print("He is a champion now in", org_name)

who = fighters()
print(who.fighter('Khamzat'))    
print(fighters().fighter('Ryu'))
print(fighters().fighter("Islam"))
print(who.fighter("Khamzat"))

