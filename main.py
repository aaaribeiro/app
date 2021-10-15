from fastapi import FastAPI, Form, Response

app = FastAPI()
 
@app.get("/helloworld")
def root():
  return {"message": "Hello World!"}


@app.post("/hook")
async def chat():
#   response = MessagingResponse()
   msg = {f"Hi, you said: ok"}
   return msg