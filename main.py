from fastapi import FastAPI, Form, Response

app = FastAPI()
 
@app.get("/hello")
def root():
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat(From: str = Form(...), Body: str = Form(...)): 
   msg = {f"Hi {From}, you said: {Body}"}
   return Response(content=str(msg), media_type="application/json")