from enum import Enum
from fastapi import FastAPI, File, UploadFile, Body, status, Depends, Form

import pandas as pd
from fastapi import FastAPI, UploadFile
from PIL import Image
from pydantic import BaseModel, validator, root_validator
from typing import Optional
from catboost import CatBoostClassifier

class MlRequest(BaseModel):
    bad_to_eat: int
    little_energy: int
    rash: int
    liquid_poop: int

app = FastAPI()

model = CatBoostClassifier()
model.load_model('static/models/parasites_catboost.cbm', format='cbm')

def make_prediction(bad_to_eat, little_energy, rash, liquid_poop):
    df = pd.DataFrame([[bad_to_eat, little_energy, rash, liquid_poop]],
                      columns=["bad_to_eat", "little_energy", "rash", "liquid_poop"])
    prediction = model.predict(df)

    preds_class = model.predict(df).tolist()
    # Get predicted probabilities for each class
    preds_proba = model.predict_proba(df)
    # Get predicted RawFormulaVal
    preds_raw = model.predict(df, prediction_type='RawFormulaVal')
    return preds_class

# https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi
@app.post("/send/poll/") # , response_model=MlRequest
async def create_upload_file(parameters: MlRequest):
    """Загрузка файла"""
    prediction = 1
    # prediction = make_prediction(parameters.bad_to_eat,
    #                              parameters.little_energy,
    #                              parameters.rash,
    #                              parameters.liquid_poop)
    prediction = make_prediction(**parameters.dict())
    return {"prediction": prediction}


class MlRequest2(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float

@app.post("/model-predict")
async def ml_predict(parameters: MlRequest2):
    prediction = "1"
    return {"prediction": prediction}