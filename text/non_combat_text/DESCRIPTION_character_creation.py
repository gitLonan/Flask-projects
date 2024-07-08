



class NonCombatText():

    def __init__(self):
        self.text = ''

    def get_text(self,text):
        if text == "char_creation":
            self.text = """
-Be aware, available classes are based on stats, you'll only be able to see and choose if your stats are sufficient
-Currently no skills and no magic

"""
            
        return self.text