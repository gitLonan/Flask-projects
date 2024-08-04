from app import app, db
import sqlalchemy as sa
from flask import render_template, redirect, url_for, request, session, flash
from app import stats
from app import non_combat_text
from app import stats_generator, treshold, create_class_instance, character, list_of_classes
from app.character_models import CharacterClass
import typing
import random



################################################################################################################



