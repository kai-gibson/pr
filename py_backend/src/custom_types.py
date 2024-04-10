from pydantic import BaseModel, PositiveInt, PositiveFloat
from datetime import datetime
from typing import List

class Set(BaseModel):
    weight: PositiveFloat
    reps: PositiveInt

class SetData(BaseModel):
    timestamp: datetime
    weight: PositiveFloat
    reps: PositiveInt
    indicator: PositiveFloat

class ExcerciseData(BaseModel):
    excercise_id: PositiveInt
    excercise_name: str

#@ /add-excercise POST body
class AddExcercise(BaseModel):
    excercise_name: str

#@ /log-excercise POST body
class LogExcercise(BaseModel):
    excercise_id: PositiveInt
    sets: List[Set]


#@ /track GET return
class TrackExcercise(BaseModel):
    data: List[SetData]

#@ /excercises GET return
class ExcercisesList(BaseModel):
    data: List[ExcerciseData]
