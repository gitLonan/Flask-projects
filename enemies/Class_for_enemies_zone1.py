import random
import os

class FillerClass():
        def __init__(self):             
                self.str = 0
                self.agi = 0
                self.con = 0
                self.int = 0
                self.wis = 0
                
                self.physical_attack = 0
                self.magical_attack = 0
                self.physical_defense = 0
                self.magical_defense = 0
                self.speed = 0
                self.max_hp = 0
                self.current_hp = 0
                self.spells = {}

                self.enemy_icon = ''

                self.high_coefficient = 1
                self.medium_coefficient = 0.7
                self.lower_coefficient = 0.3

        def get_icon(self, enemy_name) -> None:
                cwd = os.getcwd()
                directory = os.path.dirname(f"{cwd}/app/assets/enemies/zone_1/{enemy_name}/")
                list_of_icons = []
                for name in os.listdir(directory):
                        if name[-4:] == ".png":
                                list_of_icons.append(name[:-4])
                rand = random.randint(0, len(list_of_icons)-1)
                return list_of_icons[rand]
        
class Bandit(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = "Bandit"

        def set_original_stats(self):
                self.str = random.randint(3,10)
                self.agi = random.randint(3,14)
                self.int = random.randint(3,8)
                self.wis = random.randint(3,6)
                self.con = random.randint(3,8)

                self.physical_attack = round(self.str * self.high_coefficient*10)
                self.physical_defense = round(self.con * self.medium_coefficient*10 + self.str * self.lower_coefficient*10)

                self.speed = round(self.agi * self.medium_coefficient*10)
                self.max_hp = round(self.con * self.high_coefficient*10 + self.str * self.lower_coefficient*10)
                self.current_hp = self.max_hp
                self.magical_attack = round(self.int * self.high_coefficient*10 + self.wis * self.lower_coefficient*10)
                self.magical_defense = round(self.int * self.lower_coefficient*10 + self.wis * self.medium_coefficient*10)
                self.enemy_icon = self.get_icon(self.__class__.__name__)

        def exp_worth(self) -> None:
                exp = random.randint(7,14)
                self.worth_exp = exp

class Peasant(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = "Peasant"

        def set_original_stats(self):
                self.str = random.randint(3,10)
                self.agi = random.randint(1,9)
                self.int = random.randint(3,14)
                self.wis = random.randint(1,15)
                self.con = random.randint(3,5)

                self.physical_attack = round(self.str * self.high_coefficient*10)
                self.physical_defense = round(self.con * self.medium_coefficient*10 + self.str * self.lower_coefficient*10)

                self.speed = round(self.agi * self.medium_coefficient*10)
                self.max_hp = round(self.con * self.high_coefficient*10 + self.str * self.lower_coefficient*10)
                self.current_hp = self.max_hp
                self.magical_attack = round(self.int * self.high_coefficient*10 + self.wis * self.lower_coefficient*10)
                self.magical_defense = round(self.int * self.lower_coefficient*10 + self.wis * self.medium_coefficient*10)
                self.enemy_icon = self.get_icon(self.__class__.__name__)
                
        def exp_worth(self) -> None:
                exp = random.randint(2,6)
                self.worth_exp = exp


            


    