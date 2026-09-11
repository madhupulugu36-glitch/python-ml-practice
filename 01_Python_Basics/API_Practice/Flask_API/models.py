from sqlalchemy import column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from.db_connection import Base

class Item(Base):
    _tablename_ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[int] = mapped_column(Integer)