from fastapi import FastAPI, Form, Request, Response
from pydantic import BaseModel
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
"""
  "Id": 2843,
  "Type": 2,
  "Subject": "Lentidão Abertura Mapa",
  "Urgency": "Medium",
  "Status": "New",
  "Origin": 1,
  "IsDeleted": false,
  "ServiceFirstLevel": "ConnectMaster",
  "ActionCount": 1,
  "ResolvedInFirstCall": false,
  "SlaSolutionTime": 28800,
"""
class WeebhookResponse(BaseModel):
  id: int
  type_: int
  subject: str
  urgency: str
  status: str
  origin: int
  is_deleted: bool
  service_first_level: str
  action_count: int
  resolved_in_first_call: bool
  sla_solution_time: int
  actions: list
  custom_field_values: list
  weebhook_events: list


app = FastAPI()
 
@app.get("/hello")
def root():
  """
  Hello world
  """
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat(weebhook_response: WeebhookResponse):
  # print(str(request.body()))
  return weebhook_response
