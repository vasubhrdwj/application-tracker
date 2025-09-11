from sqlalchemy import Column, Integer, String, Date, Text
from src.core.db import Base
import datetime

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    job_title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    status = Column(String(50), default="applied")
    date_applied = Column(Date, default=datetime.date.today)
    notes = Column(Text, nullable=True)