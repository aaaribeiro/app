from fastapi import FastAPI, Form, Request, Response
from pydantic import BaseModel
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

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
