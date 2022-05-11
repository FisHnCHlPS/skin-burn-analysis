from fastapi import FastAPI

app = FastAPI (title = "Skin Burn Analysis")

@app.get("/")
def hello():
    return {"message":"Hello"}
