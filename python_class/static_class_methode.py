class fighters:
    def __init__(self, name):
        self.name = name

    def fight_method(self):  # Instance method
        return f"{self.name} is fighting"

    @classmethod
    def create_new_fighter(cls, name):  # Class method
        return cls(name)

    @staticmethod
    def utility_info():  # Static method
        return "Fighter class info"

# Calling an instance method
fighter1 = fighters("Islam")
print(fighter1.fight_method())

# Calling a class method
fighter2 = fighters.create_new_fighter("Khamzat")
print(fighter2.fight_method())

# Calling a static method
print(fighters.utility_info())