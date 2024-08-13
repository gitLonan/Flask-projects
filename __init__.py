from flask import Flask
from config import Config
from flask_migrate import Migrate

##### my files related imports
from app.tresh_hold_for_classes import Treshold
from app.stats_generator import Stats
from app.text.non_combat_text.DESCRIPTION_character_creation import NonCombatText
from app.character_classes import Knight, Rouge, Druid
from app.character_classes import Character


######## sqlalchemy related imports
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_sqlalchemy import SQLAlchemy
from app.battle.battlefield import Battlefild
from app.enemies.enemies import Enemy


app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
app.static_folder = app.config['STATIC_FOLDER']


stats = Stats()
treshold = Treshold()
non_combat_text = NonCombatText()
character  = Character(stats.STRENGTH, stats.AGILITY, stats.INTELLIGENCE, stats.WISDOM, stats.CONSTITUTION)
battlefield = Battlefild()
enemy = Enemy()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)

#Needed for connection managment with the database
engine = create_engine("sqlite:///app.db")

#for current in session managment
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
app.session = Session

list_of_classes = {"Knight": Knight,
                    "Rouge": Rouge,
                    "Druid": Druid,}

def create_class_instance(class_name, *args, **kwargs):
        """ Creates instance of the class that the player chose"""
        
        selected_class_object = list_of_classes[f'{class_name}']
        if selected_class_object:
            return selected_class_object(*args, **kwargs)
        return None


#####    BluePrint Register ################

from app.routess import main_menu_bp, character_creation, difficulty_settings, choose_character, zone_1
bp_main_menu = main_menu_bp(stats)
app.register_blueprint(bp_main_menu)

bp_char_creation = character_creation( character, db, stats, non_combat_text, treshold, create_class_instance)
app.register_blueprint(bp_char_creation)

bp_difficulty_settings = difficulty_settings(stats, non_combat_text)
app.register_blueprint(bp_difficulty_settings)

bp_choose_character = choose_character(db)
app.register_blueprint(bp_choose_character)

bp_zone_1 = zone_1(character, db)
app.register_blueprint(bp_zone_1)



#############################################3

from app import stats_generator, stats, treshold, create_class_instance 
from app import non_combat_text, character_models, character, battlefield, enemy

#from app import routing_url