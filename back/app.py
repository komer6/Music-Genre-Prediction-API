from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai import predict_genre, predict_alredy_exisit
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Database setup
DATABASE_URL = "sqlite:///./music.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Model
class MusicEntry(Base):
    __tablename__ = "music"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)  # 1 = Male, 0 = Female
    genre = Column(String, nullable=False)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Pydantic Models
class GenderData(BaseModel):
    age: int
    gender: str

class UserData(BaseModel):
    age: int
    gender: str  
    genre: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Convert Gender and Predict
@app.post("/convert")
def convert_gender(data: GenderData):
    ngen = 1 if data.gender.lower() == "male" else 0
    if os.path.exists('our_pridction.joblib'):
        predicted_genre = predict_alredy_exisit(data.age, ngen)
    else:
        predicted_genre = predict_genre(data.age, ngen)
    return f"Predicted genre using AI: {predicted_genre}"

# Save to SQLite instead of CSV
@app.post("/save_to_csv")
def save_to_db(data: UserData, db: Session = Depends(get_db)):
    new_entry = MusicEntry(
        age=data.age,
        gender=1 if data.gender.lower() == "male" else 0,
        genre=data.genre
    )
    db.add(new_entry)
    db.commit()
    return {"message": f"Data saved: Age: {data.age}, Gender: {data.gender}, Genre: {data.genre}"}

@app.get("/")
def home():
    return "hello"
