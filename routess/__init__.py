from flask import Blueprint


def main_menu_bp(*args, **kwargs):
    bp_main_menu = Blueprint('routess', __name__)

    from .main_menu.main_menu import init_routes
    init_routes(bp_main_menu, *args, **kwargs)

    return bp_main_menu


def character_creation(*args, **kwargs):
    bp_character_creation = Blueprint('rotuess', __name__)

    from .character_creation.character_creation import init_routes
    init_routes(bp_character_creation, *args, **kwargs)

    return bp_character_creation


    




