


class Character():
    """ Super class for all classes: inside file: character_classes.py
        """
    def __init__(self, str, agi, int, wis, con):
        self.str = str
        self.agi = agi
        self.int = int
        self.wis = wis
        self.con = con

        self.high_coefficient = 1
        self.medium_coefficient = 0.7
        self.lower_coefficient = 0.3
        self.description = " "

        self.physical_attack = round(self.str * self.high_coefficient*10)
        self.physical_defense = round(self.con * self.medium_coefficient*10 + self.str * self.lower_coefficient*10)
        self.speed = round(self.agi * self.medium_coefficient*10)
        self.hp = round(self.con * self.high_coefficient*10 + self.str * self.lower_coefficient*10)
        self.magical_attack = round(self.int * self.high_coefficient*10 + self.wis * self.lower_coefficient*10)
        self.magical_defense = round(self.int * self.lower_coefficient*10 + self.wis * self.medium_coefficient*10)

    def get_description(self):
        return " "
    
    
        
class Knight(Character):
    def __init__(self, str, agi, int, wis, con):
        super().__init__(str, agi, int, wis, con)
        
        self.description = "Warrior of love"

    def add_class_specific_stats(self):
        self.physical_defense += 40
        self.physical_attack += 10
    
    def get_description(self):
        return self.description

class Rouge(Character):
    def __init__(self, str, agi, int, wis, con):
        super().__init__(str, agi, int, wis, con)

        self.description = "This guy craaazy"

    def add_class_specific_stats(self):
        self.speed += 5

    def get_description(self):
        return self.description