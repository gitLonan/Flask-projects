from flask import current_app
from app.character_models import CharacterClass
from app import getEnemy, battlefield

class SettingUpBattle():
    """ Adds character and its enemies depending on the current zone of that said character """

    
    def setting_up_battle(character):
            """ Adds character and its enemies depending on the current zone of that said character

            Args:
                 character (class instance) - deals with the whole battle situation, go in battle/battlefield.py

            Explanation:
                First it checks if the selected character is in dic of battlefield.char_and_enemies_in_battle soo it can track different characters.id during the session of play,
                than if the character has no enemies they are created and added to the dict. If they do exist than I just get the enemy list from the dic with character.id as its key

            """
            character_name = character.name
            #dic_of_char_and_its_enemi = battlefield.char_and_enemies_in_battle
            selected_enemy = battlefield.selected_enemy_id
            #checks if selected character is in battle and if he has enemies 
            if character_name not in battlefield.char_and_enemies_in_battle.keys():
                battlefield.battle_already_ready = False
                battlefield.char_and_enemies_in_battle[character_name] = []
                
            if battlefield.char_and_enemies_in_battle[character_name] == []:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
                    battlefield.battle_already_ready = False
                    enemy_in_battle = getEnemy.get_enemy_or_enemies(character.current_zone)
                    battlefield.index = 0
                    for i in enemy_in_battle:
                            i.finialize_enemy(i)
                    battlefield.char_and_enemies_in_battle[character_name] = enemy_in_battle
                  
                    battlefield.current_battle_enemies = enemy_in_battle
                    
                    return battlefield.char_and_enemies_in_battle[character_name], selected_enemy
                
            else: 
                enemy_in_battle = battlefield.char_and_enemies_in_battle[character_name]
                battlefield.current_battle_enemies = enemy_in_battle
                return enemy_in_battle, selected_enemy
            
        
            
    def sorting_entities_regarding_speed(character):
        """ Sorts entities (char and enemies) in regards to their speed
        
        Args:
            character (class db) - row from db that corresponds with selected character
        
        """
        if battlefield.battle_already_ready == False:
            #battlefield.index = 0
            battlefield.battle_before_speed_check = []
            battlefield.battle_after_speed_check = []
            if character not in battlefield.battle_before_speed_check:
                battlefield.battle_before_speed_check.append(character)
            for i in battlefield.current_battle_enemies:
                battlefield.battle_before_speed_check.append(i)

            check = sorted(battlefield.battle_before_speed_check, key=lambda char: char.speed, reverse=True)
            for i in check:
                battlefield.battle_after_speed_check.append(i)
            battlefield.battle_already_ready = True
            print("DA VIDIMO", battlefield.char_and_enemies_in_battle)
            return 
    
    def soemthing(character):
         if battlefield.battle_already_ready == False:
              pass
           