

from app import app
from flask import render_template



@app.route('/battle')
def battle_simulation():
    # Dummy data for the character
    character = {
        'name': 'Hero',
        'hp': 120,
        'max_hp': 150,
        'exp': 340,
        'exp_to_next_level': 500,
        'physical_dmg': 25,
        'physical_def': 20,
        'speed': 18,
        'magical_attack': 30,
        'magical_defense': 15,
        'icon': 'path_to_character_icon.png'  # Replace with the actual path
    }

    # Dummy data for enemies
    enemies = [
        {
            'name': 'Goblin',
            'hp': 80,
            'max_hp': 80,
            'physical_dmg': 15,
            'physical_def': 10,
            'speed': 12,
            'magical_attack': 5,
            'magical_defense': 8,
            'icon': 'path_to_goblin_icon.png',  # Replace with the actual path
            'useful_text': 'Weak against fire spells.'
        },
        {
            'name': 'Orc',
            'hp': 150,
            'max_hp': 150,
            'physical_dmg': 35,
            'physical_def': 25,
            'speed': 10,
            'magical_attack': 8,
            'magical_defense': 12,
            'icon': 'path_to_orc_icon.png',  # Replace with the actual path
            'useful_text': 'High physical defense, but slow.'
        },
        {
            'name': 'Dragon',
            'hp': 300,
            'max_hp': 300,
            'physical_dmg': 50,
            'physical_def': 40,
            'speed': 20,
            'magical_attack': 60,
            'magical_defense': 50,
            'icon': 'path_to_dragon_icon.png',  # Replace with the actual path
            'useful_text': 'Resistant to most magic attacks.'
        }
    ]

    return render_template('battle_simulation.html', character=character, enemies=enemies)