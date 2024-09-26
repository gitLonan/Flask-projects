from app import character
import sqlalchemy as sa
from app.character_models import CharacterClass

class LoadingDB():
    def loading_in_info(char_name, db):
        query = sa.select(CharacterClass).where(CharacterClass.name == char_name)
        #print(query)
        loader = db.session.scalars(query).first()
        print(loader)
        character.str = loader.stats_STR
        character.agi = loader.stats_AGI
        character.int = loader.stats_INT
        character.wis = loader.stats_WIS
        character.con = loader.stats_CON

        

        character.high_coefficient = 1
        character.medium_coefficient = 0.7
        character.lower_coefficient = 0.3

        ### Character creation
        character.name = loader.name
        character.class_name = loader.class_name
        character.description = loader.description
        character.selected_icon = loader.icon
        character.selected_class_string = loader.class_name
        #character.class_instance = None
        #character.session_remembering = {}
        #character.cookie = 1

        ### Battle
        character.type_of_attack = ''

        ### Derived stats
        character.physical_attack = loader.physical_attack
        character.physical_defense = loader.physical_defense
        character.speed = loader.speed
        character.hp = loader.hp
        character.current_hp = loader.current_hp
        character.magical_attack = loader.magical_attack
        character.magical_defense = loader.magical_defense


        character.exp_rate = loader.exp_rate
        character.current_zone = loader.current_zone
        character.current_zone_encounter = loader.current_zone_encounter
        character.current_exp = loader.current_exp
        character.lvl = loader.level
        character.stats_points = loader.stats_points