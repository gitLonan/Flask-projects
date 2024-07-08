import random


class Stats():
    def __init__(self):

        self.STRENGTH = 0
        self.AGILITY = 0
        self.INTELLIGENCE = 0
        self.HP = 0
        self.WISDOM = 0

        self.POINTS = 4
        
        self.original_STRENGTH = 0
        self.original_AGILITY = 0
        self.original_INTELLIGENCE = 0
        self.original_HP = 0
        self.original_WISDOM = 0
        
        self.avaliable_random_gen = True
        self.isSettingOriginalStats = True

    def get_random_stats(self):
        self.STRENGTH = random.randint(3,15)
        self.AGILITY = random.randint(3,15)
        self.INTELLIGENCE = random.randint(3,15)
        self.HP = random.randint(20,35)
        self.WISDOM = random.randint(3,15)
        self.setOriginalStats()
        
    def setOriginalStats(self):
        self.original_STRENGTH += self.STRENGTH
        self.original_AGILITY += self.AGILITY
        self.original_INTELLIGENCE += self.INTELLIGENCE
        self.original_HP += self.HP
        self.original_WISDOM += self.WISDOM
        self.isSettingOriginalStats = False

    def update(self, stat, action):
        if action == "increment":
            if self.POINTS > 0:
                setattr(self,stat, getattr(self, stat) + 1)
                if stat == "HP":
                    setattr(self,stat, getattr(self, stat) + 4)
                self.POINTS -= 1
        elif action == "decrement":
            if stat == "STRENGTH" and getattr(self, stat) > self.original_STRENGTH:
                setattr(self,stat, getattr(self, stat) - 1)
                self.POINTS += 1
            elif stat == "AGILITY" and getattr(self, stat) > self.original_AGILITY:
                setattr(self,stat, getattr(self, stat) - 1)
                self.POINTS += 1
            elif stat == "INTELLIGENCE" and getattr(self, stat) > self.original_INTELLIGENCE:
                setattr(self,stat, getattr(self, stat) - 1)
                self.POINTS += 1
            elif stat == "INTELLIGENCE" and getattr(self, stat) > self.original_INTELLIGENCE:
                setattr(self,stat, getattr(self, stat) - 1)
                self.POINTS += 1
            elif stat == "HP" and getattr(self, stat) > self.original_HP:
                setattr(self,stat, getattr(self, stat) - 5)
                self.POINTS += 1
            elif stat == "WISDOM" and getattr(self, stat) > self.original_WISDOM:
                setattr(self,stat, getattr(self, stat) - 1)
                self.POINTS += 1
            

