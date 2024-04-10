from db import *
from fastapi import FastAPI
from custom_types import AddExcercise, LogExcercise, TrackExcercise
from custom_types import ExcercisesList, ExcerciseData, SetData
from sqlalchemy import desc
from datetime import datetime
from pydantic import PositiveInt

app = FastAPI()

def get_next_id(table):
    last = session.scalars(db.select(table).order_by(desc(table.id))).first()
    if last is not None:
        return last.id + 1

def get_indicator(set :TrainingLog):
    weighting = 0.3
    return set.weight + (set.reps * weighting)

@app.post("/add-excercise")
async def add_excercise(excercise: AddExcercise):
    try: 
        to_add = Excercises(id = get_next_id(Excercises), 
                           bitmask = 0,
                           name = excercise.excercise_name)
        session.add(to_add)
        session.commit()
        return {"result": "success"}
    except Exception:
        return {"error": "an error occurred"}


@app.post("/log-excercise")
async def log_excercise(log :LogExcercise):
    train_log = []

    for set in log.sets:
        try:
            train_log.append(TrainingLog(id = get_next_id(TrainingLog),
                                bitmask = 0, 
                                timestamp = datetime.now(), 
                                excercise_id = log.excercise_id,
                                reps = set.reps,
                                weight = set.weight))
        except:
            return {"error": "failed to add excercise to log"}

    try:
        session.add_all(train_log)
        session.commit()
    except:
            return {"error": "failed to add excercise to log"}


@app.get("/track-excercise")
async def track_excercises(id :PositiveInt):
    print('id received: ', id)
    data = TrackExcercise(data=[])
    response = session.scalars(db.select(TrainingLog)
                    .where(TrainingLog.excercise_id == id))
    
    for record in response:
        data.data.append(SetData(timestamp = record.timestamp,
                                 weight = record.weight,
                                 reps = record.reps,
                                 indicator = get_indicator(record)))
    return data



@app.get("/excercises")
async def excercises():
    response = ExcercisesList(data=[ExcerciseData(excercise_id=1,
                                       excercise_name="Bench Press")])

    stmt = db.select(Excercises)
    for excercise in session.scalars(stmt):
        response.data.append(ExcerciseData(excercise_id=excercise.id,
                                           excercise_name=excercise.name))
    return response
