from app import app
from flask import render_template
from flask import render_template, request, jsonify

@app.route("/")
def home_page():
    user = {'username': 'John Doe'}
    color = request.args.get('color', 'white')
    return render_template('home.html', title='Home', user=user, color=color)

@app.route('/change_color', methods=["GET"])
def change_color():
    color = request.args.get('color', 'white')
    user = {'username': 'John Doe'}
    return render_template("home.html", title="Test of Home page",user=user, color=color)

@app.route("/choose_character")
def characters():
    character1 = {
        'name': 'Character 1',
        'str': 10,
        'agi': 8,
        'int': 7,
        'hp': 100,
        'description': 'A brave warrior with unmatched strength.'
    }
    character2 = {
        'name': 'Character 2',
        'str': 8,
        'agi': 9,
        'int': 10,
        'hp': 90,
        'description': 'A cunning mage with great intellect.'
    }
    return render_template('character.html', title='Character Fight', character1=character1, character2=character2)
    
