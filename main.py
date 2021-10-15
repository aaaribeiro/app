from fastapi import FastAPI, Form, Request, Response
# import requests

app = FastAPI()
 
@app.get("/hello")
def root():
  """
  Hello world
  This is just to test the fast api's documentation features
  """
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat(request: Request):
  print(await request.body())
  return await request.json()
