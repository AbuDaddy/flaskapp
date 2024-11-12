from sqlalchemy.orm import Mapped, mapped_column
from flaskapp import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __repr__(self):
        return f"User({self.username}, {self.email})"
