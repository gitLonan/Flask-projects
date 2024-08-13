from flask import render_template,redirect, url_for
from app.character_models import CharacterClass
import sqlalchemy as sa
from flask import current_app
from app import battlefield, enemy


def init_routes(bp_zone_1, character, db):

    @bp_zone_1.route("/first_city", methods=["GET", "POST"])
    def first_city():
        if CharacterClass.character_selected == None:
            return redirect(url_for("choose_character.characters"))
        return render_template("zone_1/first_city.html")
    
    @bp_zone_1.route("/random_encounter", methods=["POST", "GET"])
    def random_encounter():
        session = current_app.session
        character = session.query(CharacterClass).filter_by(name=CharacterClass.character_selected).first()
        
        enemy_in_battle = enemy.get_enemy_or_enemies(character.current_zone)
        for i in enemy_in_battle:
            i.set_original_stats()


        #da li ovako da ostavim ili da menjam, prednost je sto zapravo vidis sta se salje u template i nekako je preglednije, a mana je sto je nekako
        #nepotrebno sa aspekta koda, ali veca preglednost zvuci kao bas dobra stvar 
        
        character = {
            'name': character.name,
            "class": character.class_name,
            'physical_dmg': character.physical_attack,
            'physical_def': character.physical_defense,
            'max_hp': character.hp,
            'hp': character.current_hp,
            'speed': character.speed,

            'magical_attack': character.magical_attack,
            'magical_defense': character.magical_defense,
            
            'exp': character.current_exp,
            'next_level_exp': 100,
            'icon': character.icon,
            "current_zone": character.current_zone,
            "current_zone_encounter": character.current_zone_encounter
        }
            

        return render_template('battle_simulation.html', character=character, enemies=enemy_in_battle)
        