from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
  return {"message": "Hello from FastAPI!"}



# uvicorn main:app --reload --port 8000