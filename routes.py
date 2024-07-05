from app import app
from flask import render_template, redirect, url_for, request
from app.stats_generator import Stats
@app.route("/main_screen")
@app.route("/", methods = ["GET", "POST"])
def home_page():
    return render_template('main_screen.html', title='Home')

@app.route("/character-creation", methods = ["GET", "POST"])
def character_creation():
    stats = Stats()
    
    #characters = {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, "wisdom": 9, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'}
    return render_template('character_creation.html', character = stats)

@app.route('/add_stat', methods=['POST'])
def add_stat():
    return redirect(url_for('character-creation'))
# @app.route('/change_color', methods=["GET"])
# def change_color():
#     color = request.args.get('color', 'white')
#     user = {'username': 'John Doe'}
#     return render_template("home.html", title="Test of Home page",user=user, color=color)

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
    
