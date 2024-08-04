from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from typing import Optional
from datetime import datetime, timezone

class CharacterClass(db.Model):
    character_selected = None
    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(12), unique=True, index=True)
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(30))
    icon: so.Mapped[str] = so.mapped_column()
    level: so.Mapped[int] = so.mapped_column()
    class_name: so.Mapped[str] = so.mapped_column()
    character_created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

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
    
    #HIDDEN STATS:
    exp_rate: so.Mapped[int] = so.mapped_column()
    critical_chance: so.Mapped[int] = so.mapped_column()





