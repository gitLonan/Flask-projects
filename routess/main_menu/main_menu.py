from flask import render_template


def init_routes(blueprint_bp, stats):
    
    @blueprint_bp.route("/")
    @blueprint_bp.route("/main_screen", methods = ["GET", "POST"])
    def main_screen():
        """ Renders the first page on the server"""
        stats.avaliable = True
        return render_template('main_menu/main_screen.html', title='Home')

