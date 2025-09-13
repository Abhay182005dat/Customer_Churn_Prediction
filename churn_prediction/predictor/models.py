from django import forms
from django.db import models

class ChurnPrediction(models.Model):
    age = models.IntegerField()
    balance = models.FloatField()
    tenure = models.IntegerField()
    num_of_products = models.IntegerField()
    estimated_salary = models.FloatField()
    credit_score = models.IntegerField()
    gender_male = models.BooleanField()
    prediction = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class ChurnPredictionForm(forms.ModelForm):
    class Meta:
        model = ChurnPrediction
        fields = ['age', 'balance', 'tenure', 'num_of_products', 
                 'estimated_salary', 'credit_score', 'gender_male']