from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())


    def __init__(self, chat_id : int):
        self.chat_id = chat_id
<<<<<<< HEAD
=======


    def __repr__(self):
        return f"User(chat_id={self.chat_id})"
>>>>>>> 01a728c (update: DDD)
    