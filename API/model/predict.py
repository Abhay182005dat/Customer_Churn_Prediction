import pandas as pd
import pickle

# Load model and scaling parameters
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

def predict_output(scaled_features: dict):
    """
    Make prediction using scaled features
    """
    try:
        # Convert dict to DataFrame
        input_df = pd.DataFrame([scaled_features])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        return prediction
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")