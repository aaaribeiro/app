from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Boolean, DateTime

from datetime import datetime
from database import Base


class Tickets(Base):
    
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(String,  ForeignKey("organizations.client_id"), nullable=False)
    status = Column(String, nullable=False)
    owner_team = Column(String, nullable=False)
    agent = Column(String, nullable=False)
    category = Column(String, nullable=False)
    urgency = Column(String, nullable=False)
    subject =  Column(String, nullable=False)


class Organizations(Base):

    __tablename__ = "organizations"

    client_id = Column(String, primary_key=True, nullable=False)
    client_name = Column(String, nullable=False)
    tickets = relationship("Tickets")


class Webhook(Base):

    __tablename__ = "webhook"

    change_id = Column(Integer, primary_key=True, nullable=False)
    change_in = Column(String, nullable=False)
    change_value = Column(String, nullable=False)
    change_status = Column(Boolean, nullable=True, default=True)
    created_date = Column(DateTime, nullable=False, default=datetime.now())