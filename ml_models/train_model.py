import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os
from datetime import datetime

BASE_DIR = os.getcwd()
DATA_PATH = os.path.join(BASE_DIR, 'hdfs_mock', 'processed_data', 'daily_avg_temp.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'ml_models', 'climate_model.pkl')

def train_model():
    if not os.path.exists(DATA_PATH):
        print("Data file not found. Run MapReduce job first.")
        return

    df = pd.read_csv(DATA_PATH)
    
    # Convert Date to Ordinal for Regression
    df['DateSeq'] = pd.to_datetime(df['Date']).map(datetime.toordinal)
    
    X = df[['DateSeq']]
    y = df['AverageTemperature']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Save Model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
        
    print(f"Model trained and saved to {MODEL_PATH}")
    print(f"Coefficient: {model.coef_[0]}")

if __name__ == "__main__":
    train_model()
