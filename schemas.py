# app/schema.py
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

# class OrganizationBase(BaseModel):
#     sk_organization: int
#     nm_organization: str


# class OrganizationCreate(OrganizationBase):
#     pass


# class Organization(OrganizationBase):
#     sk_organization: int
#     nm_organization: str

#     class Config:
#         orm_mode = True
    




# class TimeBase(BaseModel):
#     sk_data: int
#     nk_data: datetime = None
#     dt_slasolutiondate: datetime = None
#     slaresponsetime: int = None
#     dt_createddate: datetime = None
#     dt_closedin: datetime = None
#     dt_resolvedin: datetime = None


# class TimeCreate(TimeBase):
#     pass


# class Time(TimeBase):
#     sk_data: int
#     nk_data: datetime = None
#     dt_slasolutiondate: datetime = None
#     slaresponsetime: int = None
#     dt_createddate: datetime = None
#     dt_closedin: datetime = None
#     dt_resolvedin: datetime = None

#     class Config:
#         orm_mode = True




# class TicketBase(BaseModel):
#     sk_organization: int
#     sk_data: str
#     nm_ownerteam: str
#     subject: str


# class TicketCreate(TicketBase):
#     pass


# class Ticket(TicketBase):
#     sk_organization: int
#     sk_data: str
#     nm_ownerteam: str
#     subject: str

#     class Config:
#         orm_mode = True

# class PostSchema(BaseModel):
#     id: int = Field(default=None)
#     title: str = Field(...)
#     content: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "title": "Securing FastAPI applications with JWT.",
#                 "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
#             }
#         }



# class UserSchema(BaseModel):
#     fullname: str = Field(...)
#     email: EmailStr = Field(...)
#     password: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "Abdulazeez Abdulazeez Adeshina",
#                 "email": "abdulazeez@x.com",
#                 "password": "weakpassword"
#             }
#         }

# class UserLoginSchema(BaseModel):
#     email: EmailStr = Field(...)
#     password: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "abdulazeez@x.com",
#                 "password": "weakpassword"
#             }
#         }