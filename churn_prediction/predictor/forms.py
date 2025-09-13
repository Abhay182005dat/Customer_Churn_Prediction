from django import forms
from .models import ChurnPrediction

class ChurnPredictionForm(forms.ModelForm):
    class Meta:
        model = ChurnPrediction
        fields = ['age', 'balance', 'tenure', 'num_of_products', 
                 'estimated_salary', 'credit_score', 'gender_male']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter balance'}),
            'tenure': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter tenure in years'}),
            'num_of_products': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of products'}),
            'estimated_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter estimated salary'}),
            'credit_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter credit score'}),
            'gender_male': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'age': 'Age',
            'balance': 'Account Balance',
            'tenure': 'Years as Customer',
            'num_of_products': 'Number of Products',
            'estimated_salary': 'Estimated Salary',
            'credit_score': 'Credit Score',
            'gender_male': 'Male Gender',
        }
        
    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0 or age >= 120:
            raise forms.ValidationError("Age must be between 0 and 120")
        return age