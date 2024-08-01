from flask import render_template, redirect
from app.character_models import CharacterClass
import sqlalchemy as sa

def init_routes(blueprint_bp, db) -> None:

    @blueprint_bp.route("/choose_character")
    def characters():
        """
        Generate all the created characters and you can choose which you want to play
        """

        query = sa.select(CharacterClass)
        playable_characters = list(db.session.scalars(query).all())
        if characters is None:
            return redirect(url_for("/routess.main_screen"))
        return render_template('main_menu/character.html', title='Character Fight', characters=playable_characters)

