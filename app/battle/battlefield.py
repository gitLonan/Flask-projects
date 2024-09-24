


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
               
     def enemy_turn(self, enemy, character, db):
          if enemy != character:
               self.checking_type_attack(enemy, enemy.attack_type, db, character)

     def checking_type_attack(self, entity, type_attack, database, character=None):
          if entity == None:
               return
          if type_attack == "physical attack":
               self.physical_dmg(entity,database, character)



     def physical_dmg(self, entity, database, char=None):
          character = self.battle_before_speed_check[0]
          character_name = character.name

          if char == None:
               entity.current_hp -= character.get_dmg(entity)
               self.index += 1
               if entity.current_hp <= 0:
                    character.current_exp += entity.worth_exp
                    character.amount_of_killed_enemies += 1
                    
                    self.current_battle_enemies.remove(entity)
                    self.battle_after_speed_check.remove(entity)
                    print("ovo je u oduzimanju hp-a", self.current_battle_enemies, self.index)
                    self.char_and_enemies_in_battle[character_name] = self.current_battle_enemies
                    
                    
          else:
               self.index += 1
               print("DMG KOJI PRIMAM",entity.name, entity.physical_attack, entity.get_dmg(char))
               char.current_hp -= entity.get_dmg(char)
               

     
          