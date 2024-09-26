
from app.text.combat_related_text.combat_text import CombatText

class Message():
     message = ''

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
          Message.message = CombatText.message
          while True:
               if self.index > len(self.battle_after_speed_check)-1:
                    self.index = 0
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
               character_dmg = character.get_dmg(entity)
               entity.current_hp -= character_dmg
               CombatText.get_combat_text(decider='hero',enemy=entity, hero_dmg=character_dmg, character=character)
          
               self.index += 1
               if entity.current_hp <= 0:
                    CombatText.get_combat_text(decider='enemy-dead',enemy=entity, hero_dmg=character_dmg, character=character)
                    character.current_exp += entity.worth_exp
                    print(character.current_exp, character.exp_for_lvl)
                    if character.current_exp >= character.exp_for_lvl:
                         character.lvl += 1
                         character.stats_points += 1
                         character.next_lvl_exp()
                         num_list = [40,30,20,10,0]
                         for i in range(40,0, -1):
                              percent = round((character.hp/100)*i)
                              print(i, percent)
                              if character.current_hp + percent <= character.hp:
                                   character.current_hp += percent
                                   CombatText.get_combat_text(percent, decider='lvl-up', character=character)
                                   break
                    character.amount_of_killed_enemies += 1
                    
                    self.current_battle_enemies.remove(entity)
                    self.battle_after_speed_check.remove(entity)
                    self.char_and_enemies_in_battle[character_name] = self.current_battle_enemies
               
                    
                    
          else:
               self.index += 1
               enemy_dmg = entity.get_dmg(char)
               char.current_hp -= enemy_dmg
               CombatText.get_combat_text(decider='enemy',enemy=entity, enemy_dmg=enemy_dmg, character=character)
               
               

     
          