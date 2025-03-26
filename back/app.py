from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai import predict_genre, predict_alredy_exisit
import os
import pandas as pd

app = FastAPI()

# Add CORSMiddleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class GenderData(BaseModel):
    age: int
    gender: str

class UserData(BaseModel):
    age: int
    gender: str  
    genre: str

@app.post("/convert")
def convert_gender(data: GenderData):
    ngen = 1 if data.gender.lower() == "male" else 0
    if(os.path.exists('our_pridction.joblib')):
        predicted_genre = predict_alredy_exisit(data.age, ngen)
    else:
        predicted_genre = predict_genre(data.age, ngen)
    # Return the result as a string
    return f"Predicted genre using AI: {predicted_genre}"

@app.post("/save_to_csv")
def save_to_csv(data: UserData):
    # Define the file path
    file_path = 'music.csv'
    # Create a DataFrame from the user data
    new_data = pd.DataFrame([{
        'age': data.age,
        'gender': 1 if data.gender.lower() == "male" else 0,
        'genre': data.genre
    }])
    # If the file exists, append the data, otherwise create it
    if os.path.isfile(file_path):
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # If the file does not exist, create it with headers
        new_data.to_csv(file_path, mode='w', header=True, index=False)   
    # Return a response and update the model
    predict_genre(0, 0)
    return { f"Data saved: Age: {data.age}, Gender: {data.gender}, Genre: {data.genre}"}

@app.get("/")
def home():
    return "hello"
