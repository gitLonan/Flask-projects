from flask import Blueprint

"""
File for creating blueprints that will be registerd in the main app.__init__ file 

"""

def main_menu_bp(*args, **kwargs) -> Blueprint:
    bp_main_menu = Blueprint('routess', __name__)
    from .main_menu.main_menu import init_routes
    init_routes(bp_main_menu, *args, **kwargs)
    return bp_main_menu

def character_creation(*args, **kwargs):
    bp_character_creation = Blueprint('char_creation', __name__)
    from .character_creation.character_creation import init_routes
    init_routes(bp_character_creation, *args, **kwargs)
    return bp_character_creation

def difficulty_settings(*args, **kwargs) -> Blueprint:
    bp_difficulty = Blueprint("difficulty_settings", __name__)
    from .difficulty_settings.difficulty import init_routes
    init_routes(bp_difficulty, *args, **kwargs)
    return bp_difficulty

def choose_character(*args, **kwargs) -> Blueprint:
    bp_choose_character = Blueprint('choose_character', __name__)
    from .choose_character.choose_character import init_routes
    init_routes(bp_choose_character, *args, **kwargs)
    return bp_choose_character

def zone_1(*args, **kwargs) -> Blueprint:
    bp = Blueprint("zone_1", __name__)
    from .zones.zone_1 import init_routes
    init_routes(bp)
    return bp


    




