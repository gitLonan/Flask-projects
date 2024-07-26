from app.character_classes import Character, Knight, Rouge


class Treshold():
    """ 
    Holds all the stat tresholds for classes
        """

    def __init__(self):

        self.classes = {"Knight": {"str": 10, "agi": 14},
                        "Rouge": {"agi": 14},
                        
                        }

    def get_list_of_available_classes(self, character):
        """ returns available classes based on generated stats"""
        #print(character.str)
        above_treshold = []

        for class_name, stats in self.classes.items():
            token = len(stats)
            print("OVO JE TOKEN", token)
            for stat, value in self.classes[class_name].items():
                current_stat = getattr(character, stat)
                
                if not current_stat > value:
                    print(stat, value)
                    token -= 1
                    continue    
            
            if token == len(stats):
                    above_treshold.append(class_name)


        return above_treshold



