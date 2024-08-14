from app.enemies.Class_for_enemies_zone1 import Bandit, Peasant, Knight, Wizard
import random



class CreatGetEnemy():
    """ Responsible for creating instances of enemy classes and returning a list of enemies that will be used in battle"""
    def __init__(self):
        
        self.enemy = ""
        self.enemy_icon = ""
        self.enemies_in_combat = []

        self.ZONE = {"zone_1": {"Bandit": Bandit,
                             "Peasant":Peasant,
                             "Knight":Knight,
                             "Wizard":Wizard,},
                    "zone_2": {},
                    "zone_3": {},
        }
    def create_enemy_instance(self, enemy_name: str, zone: str, *args, **kwargs) -> object:
        """ Creates instance of the enemy classes"""
        
        selected_class_object = self.ZONE[zone][f'{enemy_name}']
        print("SELECTED CLASS OBJECT", selected_class_object)
        if selected_class_object:
            return selected_class_object(*args, **kwargs)
        return None
        
    def get_enemy_or_enemies(self, zone: str) -> list:
            """ Gets a list of class instances of enemies that will be in battle 
                Args:
                    zone (str): gets character.current_zone from database (such as zone_1, zone_2...)
                Returns:
                    list[enemies created for battle]: instances of classes that represent enemies 
            """
            self.enemies_in_combat = []
            num_of_enemies = random.randint(1,2)
            for i in range(num_of_enemies):  
                rand_enemy_str = random.choice(list(self.ZONE[zone]))
                rand_enemy_object = self.create_enemy_instance(rand_enemy_str,zone)
                self.enemies_in_combat.append(rand_enemy_object)
            print(self.enemies_in_combat)
            return self.enemies_in_combat