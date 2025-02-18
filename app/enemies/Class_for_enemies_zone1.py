import random
import os
from typing import Callable

class FillerClass():
        """ Holds class variables and class methods that are shareable with every class in this file"""
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
                self.id = None

                #Ovo stoji ovde jer posle zelim da ubacim i spellove, i onda kad kod nasumicno odredi da zeli da napadne ili baci spell ovo ce se menjati u zavisnosti od toga
                self.attack_type = "physical attack"

                #for derived stats
                self.high_coefficient = 0.8
                self.medium_coefficient = 0.5
                self.lower_coefficient = 0.2
                self.scale_stats = 2

        def get_icon(self, enemy_name: str) -> str:
                """ Gets random Icon for the enemy name given to the func
                Args:
                        enemy_name (str): name by which the code knows for who to look for pictures.

                Returns:
                        str: name of the picture withouth ".png" part -thats handeld dirrectly in the template.
                """

                cwd = os.getcwd()
                directory = os.path.dirname(f"{cwd}/app/assets/enemies/zone_1/{enemy_name}/")
                list_of_icons = []
                if len(os.listdir(directory)) == 0:
                        return ""
                for name in os.listdir(directory):
                        if name[-4:] == ".png":
                                list_of_icons.append(name[:-4])
                rand = random.randint(0, len(list_of_icons)-1)
                return list_of_icons[rand]     
        
        def set_original_stats(self) -> None:
                """ Sets derived stats that are based on base stats such as str, int..."""
                self.physical_attack = round(self.str * self.medium_coefficient*self.scale_stats)
                self.physical_defense = round(self.con * self.medium_coefficient*self.scale_stats + self.str * self.lower_coefficient*self.scale_stats)
                self.speed = round(self.agi * self.medium_coefficient*self.scale_stats)
                self.max_hp = round(self.con * self.high_coefficient*self.scale_stats + self.str * self.lower_coefficient*self.scale_stats)
                self.current_hp = self.max_hp
                self.magical_attack = round(self.int * self.high_coefficient*self.scale_stats + self.wis * self.lower_coefficient*self.scale_stats)
                self.magical_defense = round(self.int * self.lower_coefficient*self.scale_stats + self.wis * self.medium_coefficient*self.scale_stats)
                self.enemy_icon = self.get_icon(self.name)

        def finialize_enemy(self, object: issubclass) -> None:
                """ Updates all the stats that an enemy would need for him to be functional
                Args:
                        object (class instance): instance of the enemy class that are found in this file 
                Returns:
                        None
                """
                object.base_stats_random()
                object.set_original_stats()
                object.set_exp_gain_value()
                return
        #this is regular, i could change by adding this func to any class 
        def get_dmg(self, character):
                #trenutno svakih 50 def od 150 dodaje 20 reduction dmg, jer trenutno nisam sig da li ovako zelim da kalkulisem
                attack = round(self.physical_attack - character.physical_defense*(self.physical_defense/1000))
                return attack
        
class Bandit(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(3,10)
                self.agi = random.randint(3,14)
                self.int = random.randint(3,8)
                self.wis = random.randint(3,6)
                self.con = random.randint(3,8)

        def set_exp_gain_value(self) -> None:
                exp = random.randint(2,5)
                self.worth_exp = exp
                
                
        
        
class Peasant(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(3,5)
                self.agi = random.randint(1,6)
                self.int = random.randint(3,6)
                self.wis = random.randint(1,7)
                self.con = random.randint(3,5)
                
        def set_exp_gain_value(self) -> None:
                exp = random.randint(2,3)
                self.worth_exp = exp
                

class Knight(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(7,11)
                self.agi = random.randint(4,7)
                self.int = random.randint(5,10)
                self.wis = random.randint(5,10)
                self.con = random.randint(10,12)

                
        def set_exp_gain_value(self) -> None:
                exp = random.randint(3,6)
                self.worth_exp = exp
                

class Wizard(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(1,6)
                self.agi = random.randint(4,9)
                self.int = random.randint(8,12)
                self.wis = random.randint(8,12)
                self.con = random.randint(5,8)
                
        def set_exp_gain_value(self) -> None:
                exp = random.randint(2,6)
                self.worth_exp = exp

class Wolf(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(3,10)
                self.agi = random.randint(3,14)
                self.int = random.randint(3,8)
                self.wis = random.randint(3,6)
                self.con = random.randint(3,8)

        def set_exp_gain_value(self) -> None:
                exp = random.randint(2,5)
                self.worth_exp = exp

class Lizard(FillerClass):
        def __init__(self,*args, **kwargs):
                super().__init__(*args, **kwargs)
                self.worth_exp = 0
                self.name = self.__class__.__name__

        def base_stats_random(self):
                self.str = random.randint(3,10)
                self.agi = random.randint(3,14)
                self.int = random.randint(3,8)
                self.wis = random.randint(3,6)
                self.con = random.randint(3,8)

        def set_exp_gain_value(self) -> None:
                exp = random.randint(2,4)
                self.worth_exp = exp
                
    