from django.views import View
from django.shortcuts import render
import requests
from typing import Annotated
import pandas as pd
import json
import pickle
import os

FASTAPI_URL = 'http://localhost:8000/predict'

def predict_churn(request):
    prediction = None
    input_data = {}
    error = None

    if request.method == 'POST':
        try:
            # Extract form data
            data = {
                'Age': request.POST.get('age'),
                'Balance': request.POST.get('balance'),
                'Tenure': request.POST.get('tenure'),
                'NumOfProducts': request.POST.get('num_of_products'),
                'EstimatedSalary': request.POST.get('estimated_salary'),
                'CreditScore': request.POST.get('credit_score'),
                'Gender_Male': request.POST.get('gender_male', False)
            }


            input_data = data

            # Call FastAPI
            response = requests.post(FASTAPI_URL, json=data)

            if response.status_code == 200:
                prediction = response.json().get('prediction')
            else:
                error = f"FastAPI error: {response.text}"

        except Exception as e:
            error = str(e)

    return render(request, 'predictor/predict.html', {
        'prediction': prediction,
        'input_data': input_data,
        'error': error
    })