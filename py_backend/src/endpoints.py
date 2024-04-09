from db import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    result = session.scalars(db.select(Excercises)).first()
    if result:
        return {"id": result.id, "name": result.name}
    else:
        return {"err": "idk what happened"}



