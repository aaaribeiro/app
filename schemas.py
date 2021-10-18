# app/schema.py
from datetime import datetime
from models import Tickets, Organizations
from pydantic import BaseModel


class Ticket(BaseModel):
    ticket_id: int
    client_id: str
    status: str
    owner_team: str
    agent: str
    category: str
    urgency: str
    subject: str

    class Config:
        orm_mode = True



class Organization(BaseModel):
    client_id: str
    client_name: str

    class Config:
        orm_mode = True



class Webhook(BaseModel):
    change_id: int
    change_in: str
    change_value: str
    change_status: bool
    created_date: datetime

    class Config:
        orm_mode = True
