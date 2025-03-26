from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

import sqlite3
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

DB_PATH = "music.db"  # Path to your SQLite database

def predict_genre(age, gender):
    """Train a model using data from SQLite and predict genre based on age and gender."""
    # Connect to SQLite and fetch data
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT age, gender, genre FROM music_data"  # Assuming the table is named 'music_data'
    music_dt = pd.read_sql(query, conn)
    conn.close()

    if music_dt.empty:
        return "No data available for training"

    # Prepare the data
    X = music_dt.drop(columns=['genre'])  # Features (age, gender)
    Y = music_dt['genre']  # Target (genre)

    # Split the data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Train the model
    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    # Save the trained model
    joblib.dump(model, 'our_pridction.joblib')

    # Predict the genre
    prediction = model.predict([[age, gender]])
    return prediction[0]


def predict_alredy_exisit(age, gender):
    model=joblib.load( 'our_pridction.joblib')
    predictions= model.predict([[age,gender]])
    return predictions
