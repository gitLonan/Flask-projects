class Loadself():
        def __init__(self):
            self.str = 0
            self.agi = 0
            self.int = 0
            self.wis = 0
            self.con = 0

            self.high_coefficient = 1
            self.medium_coefficient = 0.7
            self.lower_coefficient = 0.3

            #self creation
            self.name = 0
            self.class_name = ''
            self.description = 0
            self.selected_icon = 0
            self.selected_class_string = 0
            #self.class_instance = None
            #self.session_remembering = {}
            #self.cookie = 1

            #Battle
            self.type_of_attack = ''

            #Derived stats
            self.physical_attack = 0
            self.physical_defense = 0
            self.speed = 0
            self.hp = 0
            self.current_hp = 0
            self.magical_attack = 0
            self.magical_defense = 0
            self.exp_rate = 0
        
        