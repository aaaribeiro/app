# app/api.py

from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movidesk/v1/organizations", response_model=List[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations


@app.post("/movidesk/v1/organization", response_model=schemas.Organization)
async def create_organization(organization: schemas.Organization, db: Session=Depends(get_db)):
    customer = crud.get_customer_by_id(db, id=organization.client_id)
    if customer:
        raise HTTPException(status_code=400, detail="Organization already registered")
    return crud.create_organization(db=db, organization=organization)


@app.get("/movidesk/v1/tickets", response_model=List[schemas.Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db, skip=skip, limit=limit)
    return tickets


@app.post("/movidesk/v1/ticket", response_model=schemas.Ticket)
async def create_ticket(ticket: schemas.Ticket, db: Session=Depends(get_db)):
    db_ticket = crud.get_ticket_by_id(db, id=ticket.ticket_id)
    if db_ticket:
        raise HTTPException(status_code=400, detail="Ticket already registered")
    return crud.create_ticket(db=db, ticket=ticket)


@app.post("/movidesk/v1/webhook/status", response_model=schemas.Webhook)
async def create_webhook(request: Request, db: Session=Depends(get_db)):
    db_webhook = schemas.Webhook
    db_webhook.change_id = 1
    db_webhook.change_in = "STATUS"
    db_webhook.change_value = (await request.json())["Status"]

    return crud.create_webhook(db=db, webhook=db_webhook)
    # ticket_id = (await request.json())["Id"]
    # print(ticket_id)
    # return await request.json()
