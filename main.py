from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
  return {"message": "root directory"}


@app.get("/hello")
def hello_world():
  """
  Hello world
  This is just to test the fast api's documentation features
  """
  return {"message": "Nunca esqueça você é o cara!"}


@app.post("/hook")
async def chat(request: Request):
  print(await request.json())
  return await request.json()
