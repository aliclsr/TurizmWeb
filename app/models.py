from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String, nullable=False)
    soyad = Column(String, nullable=False)
    konu = Column(String, nullable=False)
    ileti = Column(Text, nullable=False)
    tarih = Column(DateTime, default=datetime.utcnow)
