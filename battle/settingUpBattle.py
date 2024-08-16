from flask import current_app
from app.character_models import CharacterClass
from app import get_enemy

class SettingUpBattle():
     def setting_up_battle(battlefield):
          session = current_app.session
          character = session.query(CharacterClass).filter_by(name=CharacterClass.character_selected).first()
          character_id = character.id
          dict_from_battlefield = battlefield.char_and_enemies_in_battle
          selected_enemy = battlefield.selected_enemy_id
          #checks if selected character is in battle and if he has enemies 
          if character_id not in dict_from_battlefield.keys():
               dict_from_battlefield[character_id] = []
               if dict_from_battlefield[character_id] == []:
                    enemy_in_battle = get_enemy.get_enemy_or_enemies(character.current_zone)

                    for i in enemy_in_battle:
                         i.finialize_enemy(i)
                    dict_from_battlefield[character_id] = enemy_in_battle
                    battlefield.current_battle_enemies = enemy_in_battle
                    return enemy_in_battle, selected_enemy
               return enemy_in_battle, selected_enemy
          else: 
               enemy_in_battle = dict_from_battlefield[character_id]
               battlefield.current_battle_enemies = enemy_in_battle
               return enemy_in_battle, selected_enemy