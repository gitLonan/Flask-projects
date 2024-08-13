from app.enemies.Class_for_enemies_zone1 import Bandit, Peasant
import random



class Enemy():
    def __init__(self):
        
        self.enemy = ""
        self.enemy_icon = ""
        self.enemies_in_combat = []

        self.ZONE = {"zone_1": {"Bandit": Bandit,
                             "Peasant":Peasant,}
                            # "Guard":0,
                            # "Wizard":0,}
        }
    def create_enemy_instance(self, enemy_name, zone, *args, **kwargs) -> object:
        """ Creates instance of the enemy classes"""
        
        selected_class_object = self.ZONE[zone][f'{enemy_name}']
        print("SELECTED CLASS OBJECT", selected_class_object)
        if selected_class_object:
            return selected_class_object(*args, **kwargs)
        return None
        
    def get_enemy_or_enemies(self, zone) -> list:
            """ Get a list of class instances of enemies that will be in battle """
            self.enemies_in_combat = []
            num_of_enemies = random.randint(1,5)
            for i in range(num_of_enemies):  
                rand_enemy_str = random.choice(list(self.ZONE[zone]))
                rand_enemy_object = self.create_enemy_instance(rand_enemy_str,zone)
                self.enemies_in_combat.append(rand_enemy_object)
            print(self.enemies_in_combat)
            return self.enemies_in_combat

    def check_for_combat():
         pass