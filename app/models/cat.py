from sqlalchemy.orm import Mapped, mapped_column
from ..db import db, migrate

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality
        )

    @classmethod
    def from_dict(cls, cat_data):
        return Cat(
            name=cat_data["name"],
            color=cat_data["color"],
            personality=cat_data["personality"]
        )
