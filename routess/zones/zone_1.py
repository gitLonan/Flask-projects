from flask import render_template
from app.character_models import CharacterClass


def init_routes(bp_zone_1, character, db) :

    @bp_zone_1.route("/first_city", methods=["GET", "POST"])
    def first_city():
        
        return render_template("zone_1/first_city.html")
    
    @bp_zone_1.route("/random_encounter", methods=["POST", "GET"])
    def random_encounter():

        pass