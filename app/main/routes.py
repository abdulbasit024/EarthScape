from flask import render_template, jsonify
from flask_login import login_required, current_user
from app.main import bp
import pandas as pd
import os
import sys

# Add project root to sys path to import ml_models
sys.path.append(os.getcwd())
from ml_models.predict import predict_future

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Dashboard')

@bp.route('/api/climate_data')
@login_required
def climate_data():
    # Load historical data
    data_path = os.path.join(os.getcwd(), 'hdfs_mock', 'processed_data', 'daily_avg_temp.csv')
    
    historical = []
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        # Take last 30 entries for cleaner chart
        df = df.tail(30)
        historical = df.to_dict(orient='records')
        
    # Get predictions
    predictions = predict_future(days_ahead=7)
    
    return jsonify({
        'historical': historical,
        'predictions': predictions
    })
