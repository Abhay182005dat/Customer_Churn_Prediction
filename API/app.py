import pandas as pd
import numpy as np
from fastapi import FastAPI , HTTPException
from fastapi.responses import JSONResponse 
from schema.user_input import UserInput
from model.predict import MODEL_VERSION , model , predict_output
import json

app = FastAPI()



@app.get('/')
def home():
    return {'message' : 'This is FastAPI for prediction model'}


@app.get('/health')
def health_check():  # This is done for developer or machine readable purposes
    return {
        'status':'OK',
        'version': MODEL_VERSION,
        'model_loaded' : model is not None
    }




@app.post("/predict")
async def predict(data: UserInput):
    try:
        scaled_data = data.get_scaled_features()
        prediction = predict_output(scaled_data)

        return JSONResponse(
            status_code=200,
            content={'prediction': bool(prediction[0])}
        )
    
    except Exception as e:
        raise HTTPException(status_code = 500 , detail = str(e))