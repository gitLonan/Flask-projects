from flask import render_template
from flask import redirect, url_for, request, session, flash


def init_routes(blueprint_bp, stats, non_combat_text) -> None:

    @blueprint_bp.route('/select_difficulty', methods=["POST", "GET"])
    def select_difficulty():
        if request.method == "GET":
            tips = non_combat_text.get_text('tips')
        if request.method == "POST":
            tips = non_combat_text.text
            stats.current_difficulty = request.form.get('difficulty')

        return render_template('main_menu/difficulty_menu/difficulty_menu.html', selected_difficulty = stats.current_difficulty, tip_content = tips)

    @blueprint_bp.route("/next_tip", methods=["POST"])
    def next_tip():
        if request.method == "POST":
            tips = non_combat_text.get_text('tips')
        return redirect(url_for("difficulty_settings.select_difficulty"))