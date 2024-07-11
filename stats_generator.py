import random
import typing

class Stats():
    def __init__(self):

        self.STRENGTH = 0
        self.AGILITY = 0
        self.INTELLIGENCE = 0
        self.HP = 0
        self.WISDOM = 0

        self.POINTS = 0
        
        self.original_STRENGTH = 0
        self.original_AGILITY = 0
        self.original_INTELLIGENCE = 0
        self.original_HP = 0
        self.original_WISDOM = 0
        self.stats = {          "STRENGTH": "original_STRENGTH",
                                "AGILITY": "original_AGILITY",
                                "INTELLIGENCE": "original_INTELLIGENCE",
                                "HP": "original_HP",
                                "WISDOM": "original_WISDOM"
                                }
        self.difficulty = {"Baby": {
                                "STRENGTH": 3,
                                "AGILITY": 3,
                                "INTELLIGENCE": 3,
                                "HP": 10,
                                "WISDOM": 3
                                },
                            "Easy": {
                                "STRENGTH": 1,
                                "AGILITY": 1,
                                "INTELLIGENCE": 1,
                                "HP": 5,
                                "WISDOM": 1
                                },
                            "Normal": {
                                "STRENGTH": 0,
                                "AGILITY": 0,
                                "INTELLIGENCE": 0,
                                "HP": 0,
                                "WISDOM": 0
                                },
                            "Hard": {
                                "STRENGTH": -1,
                                "AGILITY": -1,
                                "INTELLIGENCE": -1,
                                "HP": -5,
                                "WISDOM": -1
                            }
        }
        self.current_difficulty = "Baby"
        
        self.avaliable_random_gen = True
        self.isSettingOriginalStats = True

    def apply_difficulty(self) -> None:
        """ Based on the difficulty values are added to the stats and then original stats are set again"""
        for stat_name,stat_value in self.difficulty[f'{self.current_difficulty}'].items():
            original_value = getattr(self, stat_name)
            for i in self.stats.keys():
                if i == stat_name: 
                    setattr(self, stat_name, original_value + stat_value) 
                    break
        self.setOriginalStats()


    def get_random_stats(self) -> None:
        self.STRENGTH = random.randint(3,15) 
        self.AGILITY = random.randint(3,15)
        self.INTELLIGENCE = random.randint(3,15)
        self.HP = random.randint(20,35)
        self.WISDOM = random.randint(3,15)
        self.POINTS = 4
        self.setOriginalStats()
        
    def setOriginalStats(self) -> None:
        self.original_STRENGTH = self.STRENGTH
        self.original_AGILITY = self.AGILITY
        self.original_INTELLIGENCE = self.INTELLIGENCE
        self.original_HP = self.HP
        self.original_WISDOM = self.WISDOM
        self.isSettingOriginalStats = False

    def update(self, stat, action):
        """ Deals with adding and descreasing stats in character creation window """
        if action == "increment":
            print("THIS IS INCREMENT",stat)
            if self.POINTS > 0:
                setattr(self,stat, getattr(self, stat) + 1)
                if stat == "HP":
                    setattr(self,stat, getattr(self, stat) + 4)
                self.POINTS -= 1

        elif action == "decrement":
            original_value = getattr(self, f"original_{stat}")
            current_value = getattr(self, stat)
            if stat in ["STRENGTH", "AGILITY", "INTELLIGENCE", "WISDOM"] and current_value > original_value:
                print("THIS IS DECREMENT",stat)
                setattr(self, stat, current_value - 1)
                self.POINTS += 1
            elif stat == "HP" and current_value > original_value:
                setattr(self, stat, current_value - 5)
                self.POINTS += 1


        

