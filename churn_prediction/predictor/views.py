from django.views import View
from django.shortcuts import render
from pydantic import BaseModel, Field
from typing import Annotated
import pandas as pd
import json
import pickle
import os

# Load model and scaling parameters
ml_folder = os.path.join(os.path.dirname(__file__), 'ml')
with open(os.path.join(ml_folder, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)
with open(os.path.join(ml_folder, 'scaling_stats.json'), 'r') as f:
    scaling_stats = json.load(f)

class UserInput(BaseModel):
    Age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    Balance: Annotated[float, Field(..., gt=-1, description='Balance in the account')]
    Tenure: Annotated[int, Field(..., gt=-1, description='Number of years you have been the client for the bank')]
    NumOfProducts: Annotated[int, Field(..., gt=-1, description='Number of products you have purchased from the bank')]
    EstimatedSalary: Annotated[float, Field(..., gt=-1, description='Your Estimated Salary')]
    CreditScore: Annotated[int, Field(..., gt=-1, description='Your credit score')]
    Gender_Male: Annotated[bool, Field(..., description='False if you are male')]

    def scale_feature(self, value, feature_name):
        stats = scaling_stats[feature_name]
        var_median = stats['median']
        quartile1 = stats['q1']
        quartile3 = stats['q3']
        interquantile_range = quartile3 - quartile1
        
        if int(interquantile_range) == 0:
            quartile1 = stats['q05']
            quartile3 = stats['q95']
            interquantile_range = quartile3 - quartile1
            if int(interquantile_range) == 0:
                quartile1 = stats['q01']
                quartile3 = stats['q99']
                interquantile_range = quartile3 - quartile1
        return round((value - var_median) / interquantile_range, 3)

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

            # Validate input using Pydantic
            user_input = UserInput(**data)
            input_data = user_input.dict()

            # Convert to DataFrame
            df = pd.DataFrame([input_data])

            # Scale numeric features
            for col in ['Age', 'Tenure', 'Balance', 'EstimatedSalary']:
                df[col] = user_input.scale_feature(df[col].values[0], col)

            # Predict
            prediction = bool(model.predict(df)[0])

        except Exception as e:
            error = str(e)

    return render(request, 'predictor/predict.html', {
        'prediction': prediction,
        'input_data': input_data,
        'error': error
    })