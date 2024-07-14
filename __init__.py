from flask import Flask
from config import Config
from app.stats_generator import Stats
from app.text.non_combat_text.DESCRIPTION_character_creation import NonCombatText
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from app.Utility.new_anotation_types import routing_url


app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
app.static_folder = app.config['STATIC_FOLDER']

character = Stats()
non_combat_text = NonCombatText()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)


from app import routes, stats_generator
from app import non_combat_text, character_models
#from app import routing_url