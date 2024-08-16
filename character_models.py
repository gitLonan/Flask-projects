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

    current_list_enemies: so.Mapped[list[str]] = so.mapped_column(MutableList.as_mutable(JSON), default=[])

    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(12), unique=True, index=True)
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(30))
    icon: so.Mapped[str] = so.mapped_column()
    level: so.Mapped[int] = so.mapped_column()
    class_name: so.Mapped[str] = so.mapped_column()
    current_exp: so.Mapped[int] = so.mapped_column(default=0)
    
    #BASE STATS
    stats_STR: so.Mapped[int] = so.mapped_column()
    stats_AGI: so.Mapped[int] = so.mapped_column()
    stats_INT: so.Mapped[int] = so.mapped_column()
    stats_CON: so.Mapped[int] = so.mapped_column()
    stats_WIS: so.Mapped[int] = so.mapped_column()
    
    #DERIVED STATS
    physical_attack: so.Mapped[int] = so.mapped_column()
    magical_attack: so.Mapped[int] = so.mapped_column()
    speed: so.Mapped[int] = so.mapped_column()
    physical_defense: so.Mapped[int] = so.mapped_column()
    magical_defense: so.Mapped[int] = so.mapped_column()
    hp: so.Mapped[int] = so.mapped_column()
    current_hp: so.Mapped[int] = so.mapped_column(default=hp)

    #HIDDEN STATS:
    exp_rate: so.Mapped[int] = so.mapped_column()
    critical_chance: so.Mapped[int] = so.mapped_column()
    character_created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    current_zone: so.Mapped[str] = so.mapped_column(default="zone_1")
    current_zone_encounter: so.Mapped[str] = so.mapped_column(default="encounter_1")
    






