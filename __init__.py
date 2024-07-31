from flask import Flask
from config import Config
from app.stats_generator import Stats
from app.text.non_combat_text.DESCRIPTION_character_creation import NonCombatText
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.tresh_hold_for_classes import Treshold
#from app.Utility.new_anotation_types import routing_url
from app.character_classes import Knight, Rouge, Druid
from app.character_classes import Character

#BluePrints import







app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
app.static_folder = app.config['STATIC_FOLDER']




stats = Stats()
treshold = Treshold()
non_combat_text = NonCombatText()
character  = Character(stats.STRENGTH, stats.AGILITY, stats.INTELLIGENCE, stats.WISDOM, stats.CONSTITUTION)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)


list_of_classes = {"Knight": Knight,
                    "Rouge": Rouge,
                    "Druid": Druid,}

def create_class_instance(class_name, *args, **kwargs):
        """ Creates instance of the class that the player chose"""
        
        selected_class_object = list_of_classes[f'{class_name}']
        if selected_class_object:
            return selected_class_object(*args, **kwargs)
        return None


#####BluePrint reg
# character, db, stats, non_combat_text, treshold, create_class_instance, CharacterClass
from app.routess import main_menu_bp
bp_main_menu = main_menu_bp(stats)
app.register_blueprint(bp_main_menu)

from app.routess import character_creation
bp_char_creation = character_creation( character, db, stats, non_combat_text, treshold, create_class_instance)
app.register_blueprint(bp_char_creation)


from app import routes, stats_generator, stats, treshold, create_class_instance 
from app import non_combat_text, character_models, character


#from app import routing_url