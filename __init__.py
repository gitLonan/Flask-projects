from flask import Flask
from config import Config


app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
app.static_folder = app.config['STATIC_FOLDER']

from app import routes