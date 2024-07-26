from app import app
from flask import render_template, redirect, url_for, request, session
from app import stats
from app import non_combat_text
from app import stats_generator, treshold, create_class_instance, character, list_of_classes

import typing
import random



############ MAIN SCREEN ##################################
@app.route("/main_screen")
@app.route("/", methods = ["GET", "POST"])
def home_page():
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



@app.route('/available_class', methods = ["POST", "GET"])
def treshold_for_classes():
    character.session_remembering = {}
    character.selected_class_string = ''
    stats.setOriginalStats()
    character.update_stats(stats)
    return redirect(url_for("choose_class"))



@app.route('/choose_class', methods = ["POST", "GET"])
def choose_class():
    
    
    classes = treshold.get_list_of_available_classes(character)
    #this is soo that python doesnt make thousands of instances of classes when user selects different ones +
    #when i add class specific stats this session remembers and i can just switch between instances of what was clicked
     
    
    
    
    selected_class_object = character

    if request.method == "POST" and request.form.get('class'):
        character.selected_class_string = request.form.get('class', default="")
        print(character.selected_class_string)

        if character.selected_class_string in character.session_remembering:
            character.cookie = 1
            stats.setOriginalStats()
            character.update_stats(stats)
            
            selected_class_object = character.session_remembering[character.selected_class_string]
            selected_class_object.add_class_specific_stats(character)
            
            
            print(character.session_remembering)
        else:
            character.cookie = 1
            selected_class_object = create_class_instance(character.selected_class_string, stats.STRENGTH, stats.AGILITY, stats.INTELLIGENCE, stats.WISDOM, stats.CONSTITUTION)
            character.session_remembering[character.selected_class_string] = selected_class_object
            stats.setOriginalStats()
            character.update_stats(stats)
            selected_class_object.add_class_specific_stats(character)
            print(character.session_remembering)

    if request.method == "POST" and request.form.get('icon'):
        #print("ASDSAD", character.session_remembering,character.selected_class_string,character.session_remembering[character.selected_class_string])
        selected_class_object = character.session_remembering[character.selected_class_string]
        character.selected_icon = request.form.get('icon')
        



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
                             selected_icon = character.selected_icon
                             )

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
    
