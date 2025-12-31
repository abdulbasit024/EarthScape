import pickle
import os
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

BASE_DIR = os.getcwd()
MODEL_PATH = os.path.join(BASE_DIR, 'ml_models', 'climate_model.pkl')

model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
    return model

def predict_future(days_ahead=7):
    if model is None:
        load_model()
        if model is None:
            return None
            
    future_dates = []
    current_date = datetime.now()
    
    predictions = []
    
    for i in range(days_ahead):
        date = current_date + timedelta(days=i)
        date_ordinal = date.toordinal()
        
        # Predict
        pred_temp = model.predict([[date_ordinal]])[0]
        
        predictions.append({
            'date': date.strftime('%Y-%m-%d'),
            'predicted_temp': round(pred_temp, 2)
        })
        
    return predictions

if __name__ == "__main__":
    preds = predict_future(5)
    print(preds)
