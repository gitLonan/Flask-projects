


class Battlefild():
     def __init__(self):
          self.selected_enemy_id = ''
          self.char_and_enemies_in_battle = {}
          self.current_battle_enemies = []

          self.char_class = None
          #ovim indexom cu ici po listi battle_after_speed_check i na taj nacin odradjivati stvari
          self.index = 0

          self.battle_before_speed_check = []
          self.battle_after_speed_check = []
          self.battle_already_ready = False
     
        

     def whos_turn_it_is(self):
         character = self.battle_before_speed_check[0]
         
         while True:
               #print("inside whos turn", self.battle_after_speed_check[self.index], len(self.battle_after_speed_check)-1,  self.index)
               if self.index > len(self.battle_after_speed_check)-1:
                    self.index = 0
               #print("OVO JE INDEX", self.index, len(self.battle_after_speed_check)-1)
               return self.battle_after_speed_check[self.index]
         print("IZASAO IS WHILE LOOPA")
               
               
     def hp_reduction(self, entity, type_attack, daatabase, char=None):
          if entity == None:
               return
          if type_attack == "physical attack":
               self.index +=1
               self.normal_dmg(entity,daatabase, char)



     def normal_dmg(self, entity,daatabase, char=None):
          character = self.battle_before_speed_check[0]
          character_id = character.id

          if char == None:
               entity.current_hp -= character.physical_attack
               if entity.current_hp <= 0:
                    
                    print("pre remove", self.current_battle_enemies)
                    self.current_battle_enemies.remove(entity)
                    self.battle_after_speed_check.remove(entity)
                    print("post remove", self.current_battle_enemies)
                    self.char_and_enemies_in_battle[character_id] = self.current_battle_enemies
                    daatabase.session.commit()
                    
          else:
               print("DMG KOJI PRIMAM",entity.name, entity.physical_attack)
               char.current_hp -= entity.physical_attack
               daatabase.session.commit()

     
          