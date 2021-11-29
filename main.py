# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:07:51 2020
@author: win10
"""
# pip install fastapi uvicorn

# 1. Library imports
import uvicorn  # ASGI
from fastapi import FastAPI
import numpy as np
import pandas as pd
from typing import Optional
from pydantic import BaseModel
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class colorclassify(BaseModel):
    red: int
    green: int
    blue: int


# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
model = tf.keras.models.load_model('colormodel_trained_90.h5')
# category color
color_dict = {
    0: 'Red',
    1: 'Green',
    2: 'Blue',
    3: 'Yellow',
    4: 'Orange',
    5: 'Pink',
    6: 'Purple',
    7: 'Brown',
    8: 'Grey',
    9: 'Black',
    10: 'White'
}


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict/')
def predict_color(feature: colorclassify):
    data = np.array([[
        feature.red,
        feature.green,
        feature.blue,
    ]])  # rgb tuple to numpy array
    # reshaping as per input to ANN model
    input_rgb = np.reshape(data, (-1, 3))
    # Output of layer is in terms of Confidence of the 11 classes
    color_class_confidence = model.predict(input_rgb)
    # finding the color_class index from confidence
    color_index = np.argmax(color_class_confidence, axis=1)
    color = color_dict[int(color_index)]
    return {
        'prediction': color
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
