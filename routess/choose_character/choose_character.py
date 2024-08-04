from flask import render_template, redirect, request, url_for
from app.character_models import CharacterClass
import sqlalchemy as sa

def init_routes(blueprint_bp, db) -> None:

    @blueprint_bp.route("/choose_character")
    def characters():
        """
        Generate all the created characters and you can choose which you want to play
        """
        chosen_char = 0
        if CharacterClass.character_selected is not None:
            chosen_char = CharacterClass.character_selected

        query = sa.select(CharacterClass)
        playable_characters = list(db.session.scalars(query).all())
        if playable_characters == []:
            return redirect(url_for("routess.main_screen"))
        return render_template('main_menu/character.html', title='Character Fight', characters=playable_characters, selected_character_id=chosen_char)
    
    @blueprint_bp.route("/selected_character", methods = ["POST"])
    def chosen_character():
        if request.method == "POST":
            chosen_char = request.form.get("character_id")
            
            #print("gledam", chosen_char, type(chosen_char))
            
            query = sa.select(CharacterClass)
            playable_characters = list(db.session.scalars(query).all())
            print(CharacterClass.character_selected, playable_characters)
            CharacterClass.character_selected = chosen_char
            
            if playable_characters == []:
                return redirect(url_for("routess.main_screen"))
            return render_template('main_menu/character.html', title='Character Fight', characters=playable_characters, selected_character_id=chosen_char)

    
    @blueprint_bp.route("/delete_character", methods = ["POST"])
    def delete_character():

        id_to_delete = request.form.get("delete_id")
        query = sa.delete(CharacterClass).where(CharacterClass.id == id_to_delete)
        db.session.execute(query)
        db.session.commit()
        print("radi", id_to_delete)
        return redirect(url_for("choose_character.characters"))