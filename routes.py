from app import app
from flask import render_template, redirect, url_for, request
from app import character
from app import non_combat_text
import typing





@app.route("/main_screen")
@app.route("/", methods = ["GET", "POST"])
def home_page():
    """ Renders the first page on the server"""

    character.avaliable = True
    return render_template('main_screen.html', title='Home')


@app.route("/character_creation", methods = ["GET", "POST"])
def character_creation():
    """ When clicked 'create character' in the menu screen, redirects to the first phase, that is stats alocation """

    if character.avaliable_random_gen == True:
        character.get_random_stats()
        character.avaliable_random_gen = False
    
    text = non_combat_text.get_text('char_creation')
    
    return render_template('character_creation.html', character = character, text=text)



@app.route('/update_stat/<stat>/<action>', methods=["GET", 'POST'])
def update_stat(stat=None, action=None): 
    """ Handels increase and descreas of stats when creating character through HTTP POST method """
    
    print(f"Received action: {action} for stat: {stat}")
    if action == "increment":
        if hasattr(character, stat):
            character.update(stat,action)
    elif action == "decrement":
        if hasattr(character, stat):
            character.update(stat, action)
    return redirect(url_for('character_creation'))

@app.route('/reroll', methods=["POST"])
def reroll():
    """Handles rerolling stats."""
    character.avaliable_random_gen = True
    return redirect(url_for('character_creation'))

@app.route("/choose_character")
def characters():
    """
    Generate all the created characters and you can choose which you want to play
    """

    characters = [
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, "wisdom": 9, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        # Add more characters here
    ]
    if characters is None:
        return redirect(url_for("/"))
    return render_template('character.html', title='Character Fight', characters=characters)
    
