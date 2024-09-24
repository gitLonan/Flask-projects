from flask import render_template
from flask import redirect, url_for, request, session, flash
import sqlalchemy as sa
from app.character_models import CharacterClass

def init_routes(blueprint_bp, character, db, stats, non_combat_text, treshold, create_class_instance) -> None:
    """
    Args:
        class: blueprint_bp - blueprint created in the init file in this folder                                                      
        class: character - instance of super class Character that has all the stats for every class                                        
        db - SQLite Alchemy database                                                                                 
        class: stats -  instance of class Stats that generates stats during character creation                                                                       
        class: non_combat_text - gets diffeerent texts that are present in character creation                               
        class: treshold - returns list of classes that the given stats meet the treshold                                                                             
    """

    @blueprint_bp.route("/character_creation", methods = ["GET", "POST"])
    def character_creation():
        """ When clicked 'create character' in the menu screen, redirects to the first phase, that is stats alocation """

        if stats.avaliable_random_gen == True:
            stats.get_random_stats()
            stats.apply_difficulty()
            stats.avaliable_random_gen = False
        
        text = non_combat_text.get_text('char_creation')
        
        return render_template('main_menu/character_creation/stats_creation.html', character = stats, text=text)

    @blueprint_bp.route('/update_stat/<stat>/<action>', methods=["GET", 'POST'])
    def update_stat(stat=None, action=None): 
        """ Handels increase and descreas of stats when creating character through HTTP POST method 
        Args:
            stat (class variable): variable thats selected for increment or decrement
            action (str): + or - button that was pressed on the template 
        """
        
        print(f"Received action: {action} for stat: {stat}")
        if action == "increment":
            if hasattr(stats, stat):
                stats.update(stat,action)
        elif action == "decrement":
            if hasattr(stats, stat):
                stats.update(stat, action)
        return redirect(url_for('char_creation.character_creation'))


    @blueprint_bp.route('/reroll', methods=["POST"])
    def reroll():
        """ Sets avaliable_random_gen = True, so when it redirects to the main template the stats will be re-rolled """
        stats.avaliable_random_gen = True
        return redirect(url_for('char_creation.character_creation'))



    @blueprint_bp.route('/setting_class_up', methods = ["POST", "GET"])
    def setting_class_up():
        character.session_remembering = {}
        character.selected_class_string = ''
        character.update_stats(stats)
        character.name = ""
        character.class_name = ""
        character.description = ""
        character.selected_class_string = ""
        character.selected_icon = ""
        return redirect(url_for("char_creation.choose_class"))



    @blueprint_bp.route('/choose_class', methods = ["POST", "GET"])
    def choose_class():
        """ Handles selection of the playable class, it's name and it's description"""
        
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
                #This is where selected_class_objects goes from being Character class to instance of a specific class you chose
                selected_class_object = create_class_instance(character.selected_class_string, stats.STRENGTH, stats.AGILITY, stats.INTELLIGENCE, stats.WISDOM, stats.CONSTITUTION)
                character.session_remembering[character.selected_class_string] = selected_class_object
                character.update_stats(stats)
                selected_class_object.add_class_specific_stats(character)
                

        if request.method == "POST" and request.form.get('icon'):
            selected_class_object = character.session_remembering[character.selected_class_string]
            character.selected_icon = request.form.get('icon')
        
        if request.method == "POST" and request.form.get("user_description"):
            try:
                selected_class_object = character.session_remembering[character.selected_class_string]
            except KeyError:
                flash("You need to select the class first!", "error")
                redirect(url_for("char_creation.choose_class"))
            character.description = request.form.get("user_description")
            print(character.description)
            
            
        if request.method == "POST" and request.form.get('character_name'):
            try:
                selected_class_object = character.session_remembering[character.selected_class_string]
                character_name = request.form.get('character_name')
                query = sa.select(CharacterClass).where(CharacterClass.name == character_name)
                print(query)
                name = list(db.session.scalars(query))
                print(name)
                if name != []:
                    flash("That name allready exists!", "error")
                else:
                    character.name = character_name
            except KeyError:
                flash("Before naming select class first!", "error")
                redirect(url_for("char_creation.choose_class"))
            
            

        print(selected_class_object)
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
                                available_icons = selected_class_object.get_icon_assets(selected_class_object),
                                selected_icon = character.selected_icon,
                                user_description = character.description,
                                character_name = character.name
                                )


    @blueprint_bp.route('/finallisation_of_creation', methods=["POST", "GET"])
    def finallisation_of_creation():
        """ Enters the needed information into the database after creating character"""

        if character.selected_class_string == "":
            flash("Before continuing select class first!", "error")
            return redirect(url_for("char_creation.setting_class_up"))
        if character.selected_icon == "":
            flash("Before continuing select your icon!", "error")
            return redirect(url_for("char_creation.setting_class_up"))
        if character.name == "":
            flash("Before continuing name your character!", "error")
            return redirect(url_for("char_creation.setting_class_up"))

        
        if character.selected_icon == "" or character.selected_class_string == "" or character.name == "":
            flash("Before continuing select class first!", "error")
            character.selected_class_string = ""
            
        
        database_class = CharacterClass(name = character.name,
                                    description = character.description,
                                    icon = character.selected_icon,
                                    level = 1,
                                    class_name = character.selected_class_string,
                                    #BASE STATS
                                    stats_STR = character.str,
                                    stats_AGI = character.agi,
                                    stats_INT = character.int,
                                    stats_CON = character.con,
                                    stats_WIS = character.wis,
                                    #DERIVED STATS
                                    physical_attack = character.physical_attack,
                                    magical_attack = character.magical_attack,
                                    speed = character.speed,
                                    physical_defense = character.physical_defense,
                                    magical_defense = character.magical_defense,
                                    hp = character.hp,
                                    current_hp = character.hp,
                                    #HIDDEN STATS
                                    exp_rate = character.exp_rate,
                                    critical_chance = 0,
                                                )
        
        db.session.add(database_class)
        db.session.commit()
        
        return redirect(url_for("routess.main_screen"))