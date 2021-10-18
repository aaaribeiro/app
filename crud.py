from sqlalchemy.orm import Session
# from sqlalchemy import func
import models, schemas


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organizations).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, id: str):
    return db.query(models.Organizations).filter(models.Organizations.client_id==id).first()


def create_organization(db: Session, organization: schemas.Organization):
    customer = models.Organizations(
        client_id = organization.client_id,
        client_name = organization.client_name
        )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def create_ticket(db: Session, ticket: schemas.Ticket):
    db_ticket = models.Tickets(
        ticket_id = ticket.ticket_id,
        client_id = ticket.client_id,
        status = ticket.status,
        owner_team = ticket.owner_team,
        agent = ticket.agent,
        category = ticket.category,
        urgency = ticket.urgency,
        subject = ticket.subject,
        )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tickets).offset(skip).limit(limit).all()


def get_ticket_by_id(db: Session, id: int):
    return db.query(models.Tickets).filter(models.Tickets.ticket_id==id).first()


# def get_webhook_max_id(db: Session):
#     return db.query(func.max(models.Webhook)).filter(models.Tickets.ticket_id==id).first()

def create_webhook(db: Session, webhook: schemas.Webhook):
    db_webhook = models.Webhook(
        change_id = webhook.change_id,
        change_in = webhook.change_in,
        change_value =  webhook.change_value,
        change_status = webhook.change_status,
        created_date = webhook.created_date
        )
    db.add(db_webhook)
    db.commit()
    db.refresh(db_webhook)
    return db_webhook