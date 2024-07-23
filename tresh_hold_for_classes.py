from app.character_classes import Character, Knight, Rouge


class Treshold():
    """ 
    Holds all the stat tresholds for classes
        """

    def __init__(self):

        self.classes = {"Knight": {"str": 10},
                        "Rouge": {"agi": 14}
                        
                        }

    def get_list_of_available_classes(self, character):
        """ returns available classes based on generated stats"""
        #print(character.str)
        above_treshold = []

        for class_name, stats in self.classes.items():
            #print("ovo gledam", class_name)
            for stat, value in self.classes[class_name].items():
                current_stat = getattr(character, stat)
                print("current stats", current_stat)
                if current_stat > value:
                    above_treshold.append(class_name)


        return above_treshold



