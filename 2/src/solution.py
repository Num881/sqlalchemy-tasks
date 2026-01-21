import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Date, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])


# BEGIN (write your solution here)
class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(256), unique=True)
    author: Mapped[str] = mapped_column(String(128))
    published_date: Mapped[datetime.date] = mapped_column(Date())
    pages: Mapped[int] = mapped_column()
    genre: Mapped[str] = mapped_column(String(64))
    rating: Mapped[float] = mapped_column(Float())
# END

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
