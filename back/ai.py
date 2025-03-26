from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

def predict_genre(age, gender):
    # Load the dataset
    music_dt = pd.read_csv('music.csv')
    
    # Prepare the data
    X = music_dt.drop(columns=['genre'])  # features (age, gender)
    Y = music_dt['genre']  # target (genre)
    
    # Split the data into train and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    
    # Initialize the decision tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)  # Train the model
    
    # Predict the genre based on input age and gender
    prediction = model.predict([[age, gender]])
    joblib.dump(model, 'our_pridction.joblib')
    
    return prediction[0]

def predict_alredy_exisit(age, gender):
    model=joblib.load( 'our_pridction.joblib')
    predictions= model.predict([[age,gender]])
    return predictions
