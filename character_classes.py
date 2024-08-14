import os


class Character():
    """ Super class for all classes: inside file: character_classes.py"""


    def __init__(self, str, agi, int, wis, con):
        self.str = str
        self.agi = agi
        self.int = int
        self.wis = wis
        self.con = con

        self.high_coefficient = 1
        self.medium_coefficient = 0.7
        self.lower_coefficient = 0.3

        self.name = ""
        self.class_name = ""
        self.description = ""
        self.selected_icon = ''
        self.selected_class_string = ""
        self.class_instance = None
        self.session_remembering = {}
        self.cookie = 1

        self.physical_attack = 0
        self.physical_defense = 0
        self.speed = 0
        self.hp = 0
        self.magical_attack = 0
        self.magical_defense = 0
        self.exp_rate = 1

    def get_description(self):
        return " "
    
    def update_stats(self, stats):
        self.str = stats.STRENGTH
        self.agi = stats.AGILITY
        self.int = stats.INTELLIGENCE
        self.wis = stats.WISDOM
        self.con = stats.CONSTITUTION

        self.physical_attack = round(self.str * self.high_coefficient*10)
        self.physical_defense = round(self.con * self.medium_coefficient*10 + self.str * self.lower_coefficient*10)
        self.speed = round(self.agi * self.medium_coefficient*10)
        self.hp = round(self.con * self.high_coefficient*10 + self.str * self.lower_coefficient*10)
        self.magical_attack = round(self.int * self.high_coefficient*10 + self.wis * self.lower_coefficient*10)
        self.magical_defense = round(self.int * self.lower_coefficient*10 + self.wis * self.medium_coefficient*10)

    def get_icon_assets(self, object):
        cwd = os.getcwd()
        print("GLEDAJ", object.name)
        directory = os.path.dirname(f"{cwd}/app/assets/classes/{object.class_name}/")
        #print(directory)
        list_of_icons = []
        for name in os.listdir(directory):
                if name[-4:] == ".png":
                    list_of_icons.append(name[:-4])
        return list_of_icons
    
        
class Knight(Character):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.description = "A disciplined warrior clad in armor, the Knight excels in both offense and defense. With unwavering courage and strength, they protect allies and vanquish foes."
        self.class_name = self.__class__.__name__

    def add_class_specific_stats(self, character):
        if character.cookie == 1:
            character.physical_defense += 20
            character.physical_attack += 10
            character.cookie = 0

    def get_description(self):
        return self.description


class Rouge(Character):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.description = "A master of stealth and agility, the Rogue excels in evasion and precision strikes. Quick and cunning, they navigate the shadows to outmaneuver and incapacitate foes."
        self.class_name = self.__class__.__name__

    def add_class_specific_stats(self, character):
        if character.cookie == 1:
            character.speed += 10
            character.cookie = 0
    
    def get_description(self):
        return self.description


class Druid(Character):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.description = "KERUSA"
        self.class_name = self.__class__.__name__

    def add_class_specific_stats(self, character):
        if character.cookie == 1:
            character.magical_attack += 20
            character.exp_rate += 0.1
            character.cookie = 0
    
    def get_description(self):
        return self.description