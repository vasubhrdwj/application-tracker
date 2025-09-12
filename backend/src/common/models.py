from sqlalchemy import Boolean, String, Date, Text
from src.core.db import Base
import datetime

from sqlalchemy.orm import Mapped, mapped_column

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(String(100), nullable=False)
    job_title: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="applied")
    date_applied: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)  # RFC 3696 max email length
    full_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)