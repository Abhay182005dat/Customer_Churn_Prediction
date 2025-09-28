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

