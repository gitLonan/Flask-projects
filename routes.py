from app import app
from flask import render_template, redirect, url_for, request, session, flash
from app import stats
from app import non_combat_text
from app import stats_generator, treshold, create_class_instance, character, list_of_classes
from app.character_models import CharacterClass
import typing
import random



############ MAIN SCREEN ##################################
@app.route("/")
@app.route("/main_screen", methods = ["GET", "POST"])
def main_screen():
    """ Renders the first page on the server"""

    stats.avaliable = True
    return render_template('main_menu/main_screen.html', title='Home')
##########################





############ Character Creation Related ##################################
@app.route("/character_creation", methods = ["GET", "POST"])
def character_creation():
    """ When clicked 'create character' in the menu screen, redirects to the first phase, that is stats alocation """

    if stats.avaliable_random_gen == True:
        stats.get_random_stats()
        stats.apply_difficulty()
        stats.avaliable_random_gen = False
    
    text = non_combat_text.get_text('char_creation')
    
    return render_template('main_menu/character_creation/stats_creation.html', character = stats, text=text)

@app.route('/update_stat/<stat>/<action>', methods=["GET", 'POST'])
def update_stat(stat=None, action=None): 
    """ Handels increase and descreas of stats when creating character through HTTP POST method """
    
    print(f"Received action: {action} for stat: {stat}")
    if action == "increment":
        if hasattr(stats, stat):
            stats.update(stat,action)
    elif action == "decrement":
        if hasattr(stats, stat):
            stats.update(stat, action)
    return redirect(url_for('character_creation'))


@app.route('/reroll', methods=["POST"])
def reroll():
    """Handles rerolling stats."""
    stats.avaliable_random_gen = True
    return redirect(url_for('character_creation'))



@app.route('/setting_class_up', methods = ["POST", "GET"])
def setting_class_up():
    character.session_remembering = {}
    character.selected_class_string = ''
    character.update_stats(stats)
    character.selected_class_string = ""
    character.selected_icon = ""
    return redirect(url_for("choose_class"))



@app.route('/choose_class', methods = ["POST", "GET"])
def choose_class():
    """ Func that handels class, icon selection and description writing"""
    
    classes = treshold.get_list_of_available_classes(character)
    selected_class_object = character

    if request.method == "POST" and request.form.get('class'):
        character.selected_class_string = request.form.get('class', default="")
        if character.selected_class_string in character.session_remembering:
            character.cookie = 1
            character.update_stats(stats)
            selected_class_object = character.session_remembering[character.selected_class_string]
            selected_class_object.add_class_specific_stats(character)
        else:
            character.cookie = 1
            selected_class_object = create_class_instance(character.selected_class_string, stats.STRENGTH, stats.AGILITY, stats.INTELLIGENCE, stats.WISDOM, stats.CONSTITUTION)
            character.session_remembering[character.selected_class_string] = selected_class_object
            character.update_stats(stats)
            selected_class_object.add_class_specific_stats(character)
            

    if request.method == "POST" and request.form.get('icon'):
        selected_class_object = character.session_remembering[character.selected_class_string]
        character.selected_icon = request.form.get('icon')
    
    if request.method == "POST" and request.form.get("user_description"):
        selected_class_object = character.session_remembering[character.selected_class_string]
        character.description = request.form.get("user_description")
        print(character.description)
        
    return render_template("main_menu/character_creation/class_choice.html",
                             available_classes = classes,
                             class_description = selected_class_object.description,
                             physical_attack = character.physical_attack,
                             magic_attack = character.magical_attack,
                             physical_defense = character.physical_defense,
                             magical_defense = character.magical_defense,
                             health = character.hp,
                             speed = character.speed,
                             selected_class=character.selected_class_string,
                             available_icons = selected_class_object.get_icon_assets(),
                             selected_icon = character.selected_icon,
                             user_description = character.description
                             )

@app.route('/finallisation_of_creation', methods=["POST", "GET"])
def finallisation_of_creation():
    """ Enters the needed information into the database after creating character"""

    
    if character.selected_icon == "" or character.selected_class_string == "":
        character.selected_class_string = ""
        return redirect(url_for("setting_class_up"))
    
    database_class = CharacterClass(name = "Muad'Dib",
                                class_name = "asd")
    
    return redirect(url_for("main_screen"))

##############################################################








############ Set difficulty  #################################
@app.route('/select_difficulty', methods=["POST", "GET"])
def select_difficulty():
    if request.method == "GET":
        tips = non_combat_text.get_text('tips')
    if request.method == "POST":
        tips = non_combat_text.text
        stats.current_difficulty = request.form.get('difficulty')

    return render_template('main_menu/difficulty_menu/difficulty_menu.html', selected_difficulty = stats.current_difficulty, tip_content = tips)

@app.route("/next_tip", methods=["POST"])
def next_tip():
    if request.method == "POST":
        tips = non_combat_text.get_text('tips')
    return redirect(url_for("select_difficulty"))
########################################################






##############################   Starting game   #################################################################
@app.route("/choose_character")
def characters():
    """
    Generate all the created characters and you can choose which you want to play
    """

    characters = [
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'con': 100, "wisdom": 9, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'con': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'con': 12, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'con': 80, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'con': 1000, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'con': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        # Add more characters here
    ]
    if characters is None:
        return redirect(url_for("/"))
    return render_template('main_menu/character.html', title='Character Fight', characters=characters)
    
################################################################################################################