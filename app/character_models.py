from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Column, String, Integer, JSON

class CharacterClass(db.Model):
    #Kad hoces da dodas ili promeni neku kolonu VIDI DA LI TREBA I U FAZI GDE INICIJALIZUJES PODATKE ZA OVU KLASU
    character_selected = None
    attack_type = ''

    

    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(12), unique=True, index=True)
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(30), nullable=True)
    icon: so.Mapped[str] = so.mapped_column(nullable=True)
    level: so.Mapped[int] = so.mapped_column(nullable=True)
    class_name: so.Mapped[str] = so.mapped_column(nullable=True)
    current_exp: so.Mapped[int] = so.mapped_column(default=0)
    
    #BASE STATS
    stats_STR: so.Mapped[int] = so.mapped_column(nullable=True)
    stats_AGI: so.Mapped[int] = so.mapped_column(nullable=True)
    stats_INT: so.Mapped[int] = so.mapped_column(nullable=True)
    stats_CON: so.Mapped[int] = so.mapped_column(nullable=True)
    stats_WIS: so.Mapped[int] = so.mapped_column(nullable=True)
    
    #DERIVED STATS
    physical_attack: so.Mapped[int] = so.mapped_column(nullable=True)
    magical_attack: so.Mapped[int] = so.mapped_column(nullable=True)
    speed: so.Mapped[int] = so.mapped_column(nullable=True)
    physical_defense: so.Mapped[int] = so.mapped_column(nullable=True)
    magical_defense: so.Mapped[int] = so.mapped_column(nullable=True)
    hp: so.Mapped[int] = so.mapped_column(nullable=True)
    current_hp: so.Mapped[int] = so.mapped_column(nullable=True)

    #HIDDEN STATS:
    exp_rate: so.Mapped[int] = so.mapped_column(nullable=True)
    stats_points: so.Mapped[int] = so.mapped_column(nullable=True, default=0)
    critical_chance: so.Mapped[int] = so.mapped_column(nullable=True)
    character_created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    current_zone: so.Mapped[str] = so.mapped_column(default="zone_1")
    current_zone_encounter: so.Mapped[str] = so.mapped_column(default="encounter_1")
    






