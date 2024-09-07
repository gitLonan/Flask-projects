import random



class NonCombatText():

    def __init__(self):
        self.text = ''
    

    def get_text(self,text):

            def before_start_of_game(self, text) -> str:
                if text == "char_creation":
                    self.text = """
        -Be aware, available classes are based on stats, you'll only be able to see and choose if your stats are sufficient
        -Currently no skills and no magic

        """
                elif text == "tips":
                    tips = [
                                "Tip 1: Remember to save your game frequently.",
                                "Tip 2: Explore every corner for hidden items.",
                                "Tip 3: Use potions wisely to conserve health.",
                            ]
                    self.text = tips[random.randint(0,2)]
                return
            
        

            before_start_of_game(self, text)
            return self.text