# EarthScape Climate Agency System

## Overview
This project is a web-based platform for the EarthScape Climate Agency to monitor and analyze climate data. It features user authentication, simulated big data processing (MapReduce), machine learning for trend prediction, and a real-time dashboard.

## Requirements
- Python 3.8+
- Flask
- Pandas
- Scikit-learn

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   The database `site.db` will be created automatically (or run `flask shell` -> `db.create_all()` if needed, though not strictly implemented in `run.py` auto-init, usually good to do).
   *Note: For this demo, just running the app creates the db context usually if configured, but let's manual init if needed.*
   Actually, `db.create_all()` should be run via python shell.

3. **Simulate Data Ingestion**
   ```bash
   python data_processing/ingestion/ingest_mock_data.py
   ```

4. **Run MapReduce Job**
   ```bash
   python data_processing/mapreduce/local_runner.py
   ```

5. **Train Model**
   ```bash
   python ml_models/train_model.py
   ```

6. **Run Application**
   ```bash
   python run.py
   ```
   Access at `http://127.0.0.1:5000/`

## Features
- **Authentication**: Admin and Analyst roles.
- **Data Processing**: Custom MapReduce implementation for local execution.
- **Analytics**: Linear Regression model for temperature forecasting.
- **Visualization**: Chart.js dashboard showing historical and predicted data.
