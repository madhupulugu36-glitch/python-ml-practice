from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    course: Mapped[str] = mapped_column(String(50))