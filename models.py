from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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
