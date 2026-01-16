from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import CHAR
import uuid
from datetime import datetime

# IMPORTANT: REMOVE THE DOT HERE
from database import Base

class Interaction(Base):
    __tablename__ = "hcp_interactions"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    hcp_name = Column(String(255))
    interaction_type = Column(String(100))
    purpose = Column(String(500))
    samples_given = Column(Boolean)
    follow_up_date = Column(String(50))
    summary = Column(String(1000))
    created_at = Column(DateTime, default=datetime.utcnow)
