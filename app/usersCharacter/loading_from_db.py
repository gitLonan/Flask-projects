from app import create_class_instance
from app import character


class LoadingDB():
    def loading_in_info(database_character):
        character.str = database_character.stats_STR
        character.agi = database_character.stats_AGI
        character.int = database_character.stats_INT
        character.wis = database_character.stats_WIS
        character.con = database_character.stats_CON

        character.high_coefficient = 1
        character.medium_coefficient = 0.7
        character.lower_coefficient = 0.3

        #Character creation
        character.name = database_character.name
        character.class_name = ''
        character.description = database_character.description
        character.selected_icon = database_character.icon
        character.selected_class_string = database_character.class_name
        #character.class_instance = None
        #character.session_remembering = {}
        #character.cookie = 1

        #Battle
        character.type_of_attack = ''

        #Derived stats
        character.physical_attack = database_character
        character.physical_defense = database_character
        character.speed = database_character
        character.hp = database_character
        character.current_hp = 0
        character.magical_attack = database_character
        character.magical_defense = database_character
        character.exp_rate = database_character
