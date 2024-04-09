import sqlalchemy as db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class TrainingLog(Base):
    __tablename__ = "training_log"
    id: Mapped[int] = mapped_column(primary_key=True)
    bitmask: Mapped[int] = mapped_column()
    timestamp :Mapped[str] = mapped_column(String(20))
    excercise_id :Mapped[int] = mapped_column(ForeignKey("excercises.id"))
    reps :Mapped[int] = mapped_column()
    weight :Mapped[float] = mapped_column()

    def __repr__(self) -> str:
        return f"""TrainingLog(id={self.id!r}, bitmask={self.bitmask!r}, timestamp={self.timestamp!r}, excercise_id={self.excercise_id!r}, reps={self.reps!r}, weight={self.weight!r})"""

class Excercises(Base):
    __tablename__ = "excercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    bitmask: Mapped[int] = mapped_column()
    name: Mapped[String] = mapped_column(String(40))

    def __repr__(self) -> str:
        return f"""TrainingLog(id={self.id!r}, bitmask={self.bitmask!r}, name={self.name!r}"""

engine = db.create_engine("sqlite:///excercise_database.sqlite")
conn = engine.connect()

Base.metadata.create_all(engine)
session = Session(engine)

#session.add(Excercises(id=1, bitmask=0, name="Bench Press"))
#session.add(Excercises(id=2, bitmask=1, name="EZ Bar Curls"))
#session.commit()

#stmt = db.select(Excercises)
#for excercise in session.scalars(stmt):
#    print(excercise)

#TrainingLog = db.Table('training_log', metadata,
#                        db.Column('id', db.Integer(), primary_key=True),
#                        db.Column('bitmask', db.Integer(), primary_key=True),
#                        db.Column('timestamp', db.DateTime()),
#                        db.Column('excercise_id', db.Integer()),
#                        db.Column('reps', db.Integer()), 
#                        db.Column('weight', db.Integer())
#                        ) 
#
#Excercises = db.Table('excercises', metadata,
#                        db.Column('id', db.Integer(), primary_key=True),
#                        db.Column('bitmask', db.Integer(), primary_key=True),
#                        db.Column('name', db.String()),
#                        ) 


