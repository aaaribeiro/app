from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/helloworld/")
def root ():
  return {"message": "Hello World!"}