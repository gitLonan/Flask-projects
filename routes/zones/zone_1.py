from flask import render_template,redirect, url_for, request
from app.character_models import CharacterClass
import sqlalchemy as sa
from flask import current_app
from app import battlefield, getEnemy, character
from app import db
from app.battle.settingUpBattle import SettingUpBattle

def init_routes(bp_zone_1):
    """ Outer func is needed for importing into local __init__ file soo I can app.register_blueprint in the main __init__

    Args:
        bp_zone_1 (class)- blueprint created in the init file in this folder                                                      
                                         
    """
    @bp_zone_1.route("/first_city", methods=["GET", "POST"])
    def first_city():
        if CharacterClass.character_selected == None:
            return redirect(url_for("choose_character.characters"))
        print('just to see, shouldnt be zero', character.str)
        battlefield.selected_enemy_id = ''
        battlefield.battle_after_speed_check = []
        battlefield.battle_before_speed_check = []
        return render_template("zone_1/first_city.html")
    
    @bp_zone_1.route("/random_encounter", methods=["POST", "GET"])
    def random_encounter():
        """ Loads character from session, loads enemies and registers them with the battlefield class for further battle computing"""
        session = current_app.session
        character = session.query(CharacterClass).filter_by(name=CharacterClass.character_selected).first()

        enemy_in_battle, selected_enemy = SettingUpBattle.setting_up_battle(character)
        SettingUpBattle.sorting_entities_regarding_speed(character)
        character = battlefield.battle_before_speed_check[0]
        #da li ovako da ostavim ili da menjam, prednost je sto zapravo vidis sta se salje u template i nekako je preglednije, a mana je sto je nekako
        #nepotrebno sa aspekta koda, ali veca preglednost zvuci kao bas dobra stvar 
        char = {
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
        return render_template('battle_simulation.html', character = char, enemies = enemy_in_battle, selected_enemy = selected_enemy)
        
    @bp_zone_1.route("/selected_enemy", methods=["POST", "GET"])
    def selected_enemy():
            character = battlefield.battle_before_speed_check[0]
            print(character)
        
            battlefield.selected_enemy = ""
            enemy_selected = request.form.get("enemy_id")
            battlefield.selected_enemy_id = int(enemy_selected)

            #entity_for_attacking = battlefield.whos_turn_it_is()


                

            return redirect(url_for("zone_1.random_encounter"))
 
        
    @bp_zone_1.route("/attack", methods=["POST", "GET"])
    def attack():
        session = current_app.session
        character = session.query(CharacterClass).filter_by(name=CharacterClass.character_selected).first()

        enemy_id = battlefield.selected_enemy_id
        current_enemy_object = None

        for enemy in battlefield.current_battle_enemies:
            if enemy.id == enemy_id:
                current_enemy_object = enemy
                break
        character.attack_type = "physical attack"
        battlefield.hp_reduction(current_enemy_object, character.attack_type)
        return redirect(url_for("zone_1.random_encounter"))
    
    

    @bp_zone_1.route("/enemy_turn", methods=["POST", "GET"])
    def enemy_turn():
        
        return redirect(url_for("zone_1.random_encounter"))