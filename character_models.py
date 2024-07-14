from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from typing import Optional
from datetime import datetime, timezone

class CharacterClass(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(12), unique=True, index=True)
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(30))
    stats_STR: so.Mapped[int] = so.mapped_column()
    stats_AGI: so.Mapped[int] = so.mapped_column()
    stats_INT: so.Mapped[int] = so.mapped_column()
    stats_HP: so.Mapped[int] = so.mapped_column()
    stats_WIS: so.Mapped[int] = so.mapped_column()
    character_created: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    icon: so.Mapped[str] = so.mapped_column()

    level: so.Mapped[int] = so.mapped_column()






