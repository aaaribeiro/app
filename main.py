from fastapi import FastAPI, Form, Request, Response
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

app = FastAPI()
 
@app.get("/hello")
def root():
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat(request: Request):
  return await request.json()
