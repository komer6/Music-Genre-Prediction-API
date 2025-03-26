import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ai import predict_genre, predict_alredy_exisit
from app import MusicEntry, Base

# Set up the database
DATABASE_URL = "sqlite:///./music.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

def load_data_from_csv_to_db(csv_file: str):
    # Read data from the CSV file
    music_data = pd.read_csv(csv_file)
    
    # Make sure the required columns are present
    if 'age' not in music_data.columns or 'gender' not in music_data.columns or 'genre' not in music_data.columns:
        print("CSV file must have 'age', 'gender', and 'genre' columns")
        return
    
    # Open a session to interact with the database
    with Session(engine) as session:
        # Loop through the rows and insert data into the database
        for _, row in music_data.iterrows():
            new_entry = MusicEntry(
                age=row['age'],
                gender=1 if row['gender'].lower() == "male" else 0,
                genre=row['genre']
            )
            session.add(new_entry)
        
        # Commit the transaction
        session.commit()
        print(f"Successfully inserted {len(music_data)} rows into the database.")
        
# Call the function to load data from the CSV file into the database
load_data_from_csv_to_db("music.csv")
