from fastapi import FastAPI, Form, Request, Response
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

app = FastAPI()
 
@app.get("/hello")
def root():
  """
  Hello world
  """
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat(request: Request):
  print(str(request.body()))
  return await request.body()
