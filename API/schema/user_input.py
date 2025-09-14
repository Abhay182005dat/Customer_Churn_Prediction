from pydantic import BaseModel, Field
from typing import Annotated
import json
import os

current_dir = os.path.dirname(os.path.dirname(__file__))
scaling_stats_path = os.path.join(current_dir, 'scaling_stats.json')

# Load or define your training data statistics
with open(scaling_stats_path, 'r') as f:
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

    def get_scaled_features(self):
        data = self.dict()
        
        for col in ['Age', 'Tenure', 'Balance', 'EstimatedSalary']:
            data[col] = self.scale_feature(data[col], col)
        return data