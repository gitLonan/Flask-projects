from app import app
from flask import render_template
from flask import render_template, request, jsonify

@app.route("/", methods = ["GET", "POST"])
def home_page():
    return render_template('main_screen.html', title='Home')

@app.route('/change_color', methods=["GET"])
def change_color():
    color = request.args.get('color', 'white')
    user = {'username': 'John Doe'}
    return render_template("home.html", title="Test of Home page",user=user, color=color)

@app.route("/choose_character")
def characters():
    characters = [
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png', 'image': 'character2.png'},
        {'name': 'Character 1', 'str': 10, 'agi': 8, 'int': 7, 'hp': 100, 'description': 'A brave warrior from the east. Fighting to survive in this lands', 'image': 'character1.png'},
        {'name': 'Character 2', 'str': 7, 'agi': 10, 'int': 9, 'hp': 80, 'description': 'A swift rogue.', 'image': 'character2.png'},
        # Add more characters here
    ]
    return render_template('character.html', title='Character Fight', characters=characters)
    
