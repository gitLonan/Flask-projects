from app.enemies.Class_for_enemies_zone1 import Bandit, Peasant, Knight, Wizard, Wolf, Lizard
import random

from app.enemies.enemy_id_storage import Id

class CreatGetEnemy():
    """ Responsible for creating instances of enemy classes and returning a list of enemies that will be used in battle"""
    def __init__(self):
        
        self.enemy = ""
        self.enemy_icon = ""
        self.enemies_in_combat = []

        self.ZONE = {"zone_1": {"Bandit": Bandit,
                             "Peasant":Peasant,
                             "Wolf": Wolf,
                             "Lizard": Lizard,
                             "Knight":Knight,
                             "Wizard":Wizard,},
                    "zone_2": {},  
                    "zone_3": {},
        }
    def create_enemy_instance(self, enemy_name: str, current_zone: str, *args, **kwargs) -> object:
        """ Creates instance of the enemy classes
            Args:
                enemy_name (str) - currently by name its reffering to the name of the class(because the name is set with __class_.__name__), check if its still like that
                current_zone (str) - where character is
        """
        #creating instance of the class from dic self.ZONE
        selected_class_object = self.ZONE[current_zone][f'{enemy_name}']
        if selected_class_object:
            enemy = selected_class_object(*args, **kwargs)
            enemy_id = random.randint(1,1000)
            while enemy_id not in Id.get_list_id(Id):
                 enemy_id = random.randint(1,1000)
                 Id.id_list.append(enemy_id)
            enemy.id = enemy_id
            return enemy
        return None
        
    def get_enemy_or_enemies(self, current_zone: str) -> list:
            """ Gets a list of class instances of enemies that will be in battle 
                Args:
                    zone (str): gets character.current_zone from database (such as zone_1, zone_2...)
                Returns:
                    list[enemies created for battle]: instances of classes that represent enemies 
            """
            self.enemies_in_combat = []
            num_of_enemies = random.randint(1,2)
            for i in range(num_of_enemies):  
                rand_enemy_str = random.choice(list(self.ZONE[current_zone]))
                rand_enemy_object = self.create_enemy_instance(rand_enemy_str,current_zone)
                self.enemies_in_combat.append(rand_enemy_object)
            #print(self.enemies_in_combat)
            return self.enemies_in_combat