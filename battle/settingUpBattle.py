from flask import current_app
from app.character_models import CharacterClass
from app import getEnemy, battlefield

class SettingUpBattle():
    """ Adds character and its enemies depending on the current zone of that said character """
    def setting_up_battle(character):
            """ Adds character and its enemies depending on the current zone of that said character

            Args:
                 battlefield (class instance) - deals with the whole battle situation, go in battle/battlefield.py

            Explanation:
                First it checks if the selected character is in dic of battlefield.char_and_enemies_in_battle soo it can track different characters during the session of play,
                than if the character has no enemies they are created and added to the dict. If they do exist than I just get the enemy list from the dic with character as its key

            """
            character_id = character.id
            dic_of_char_and_its_enemies = battlefield.char_and_enemies_in_battle
            selected_enemy = battlefield.selected_enemy_id
            #checks if selected character is in battle and if he has enemies 
            if character_id not in dic_of_char_and_its_enemies.keys():
                dic_of_char_and_its_enemies[character_id] = []
                if dic_of_char_and_its_enemies[character_id] == []:
                    enemy_in_battle = getEnemy.get_enemy_or_enemies(character.current_zone)

                    for i in enemy_in_battle:
                            i.finialize_enemy(i)
                    dic_of_char_and_its_enemies[character_id] = enemy_in_battle
                    battlefield.current_battle_enemies = enemy_in_battle
                    return enemy_in_battle, selected_enemy
                return enemy_in_battle, selected_enemy
            else: 
                enemy_in_battle = dic_of_char_and_its_enemies[character_id]
                battlefield.current_battle_enemies = enemy_in_battle
                return enemy_in_battle, selected_enemy
            
    def sorting_entities_regarding_speed(self, character):
        """ Sorts entities (char and enemies) in regards to their speed
        
        Args:
            character (class db) - row from db that corresponds with selected character
        
        """
        battlefield.battle_before_speed_check.append(character)
        for i in battlefield.current_battle_enemies:
            battlefield.battle_before_speed_check.append(i)
        battlefield.speed_check()