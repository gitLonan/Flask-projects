








class Battlefild():
     def __init__(self):
          self.selected_enemy_id = ''
          self.char_and_enemies_in_battle = {}
          self.current_battle_enemies = []

          #ovim indexom cu ici po listi battle_after_speed_check i na taj nacin odradjivati stvari
          self.index = 0

          self.battle_before_speed_check = []
          self.battle_after_speed_check = []

     def speed_check(self) -> None:
        check = sorted(self.battle_before_speed_check, key=lambda char: char.speed, reverse=True)
        for i in check:
            self.battle_after_speed_check.append(i)

     def whos_turn_it_is(self):
         character = self.battle_before_speed_check[0]
         
         while self.battle_after_speed_check[self.index] != len(self.battle_after_speed_check)-1:
               print("inside whos turn", self.battle_after_speed_check[self.index])
               if object == character:
                    self.index +=1
                    return object
               else:
                    self.index += 1
                    return object 
               
     def hp_reduction(self, entity, type_attack, char=None):
          if type_attack == "physical attack":
               self.normal_dmg(entity, char=None)



     def normal_dmg(self, entity, char=None):
          character = self.battle_before_speed_check[0]
          character_id = character.id

          if char == None:
               entity.current_hp -= character.physical_attack
               if entity.current_hp <= 0:
                    self.char_and_enemies_in_battle[character_id].remove(entity)
                    print(self.char_and_enemies_in_battle[character_id])
          else:
               char.current_hp -= entity.physical_attack
             
     
     
          