# Customer Churn Prediction

Predict whether a customer will churn using machine learning. This project includes data preprocessing, model training with LightGBM, and a REST API for predictions using FastAPI. Docker support is included for easy deployment.


## Project Structure

Customer_Churn_Prediction/
```
├── API/
│ ├── app.py
│ ├── model/
│ │ └── predict.py
│ └── requirements.txt
├── churn_prediction/
│ ├── data/
│ ├── train.py
│ └── model.pkl
├── README.md
└── .gitignore
```
---

## Features
- Preprocess and clean customer data  
- Train LightGBM model for churn prediction  
- REST API for serving predictions with FastAPI  
- Dockerized deployment for portability  

---

## 🏁 Quickstart (run the fastapi and django in separate terminals)

### 1. FastAPI ML Service

```bash
cd API
pip install -r requirements.txt
uvicorn app:app --reload
```
- The API will be available at [http://localhost:8000](http://localhost:8000)
- Test health: [http://localhost:8000/health](http://localhost:8000/health)
- Predict endpoint: `POST http://localhost:8000/predict`

### 2. Django Web App

```bash
cd churn_prediction
pip install -r requirements.txt
python manage.py runserver
```
- Visit http://localhost:8000 for the web UI

---

## 🐳 Docker (for FastAPI)

Build and run the FastAPI service:
```bash
cd API
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

---

