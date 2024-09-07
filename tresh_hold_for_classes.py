


class Treshold():
    """ 
    Holds all the stat tresholds for classes
        """

    def __init__(self):
        self.classes = {"Knight": {"str": 10,},
                        "Rouge": {"agi": 12},
                        "Druid": {"wis": 12, "int": 12},
                        "Mage": {"wis":10, "int": 10},
                        }


    def get_list_of_available_classes(self, character):
        """ returns available classes based on generated stats"""

        above_treshold = []
        for class_name, stats in self.classes.items():
            token = len(stats)
            
            for stat, value in self.classes[class_name].items():
                current_stat = getattr(character, stat)
                if not current_stat >= value:
                    token -= 1
                    continue    
            
            if token == len(stats):
                    above_treshold.append(class_name)


        return above_treshold



