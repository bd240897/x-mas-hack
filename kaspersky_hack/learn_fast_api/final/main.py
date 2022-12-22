from datetime import datetime
from enum import Enum
from fastapi import FastAPI, UploadFile, HTTPException, status, Depends, Body, Form
from PIL import Image
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from starlette.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
import secrets

from ml_models.filter.alexnet.FilterBaseline import BaseLine
from ml_models.poll.catboost.PollBaseline import PollBaseline

# инициализация приложения
app = FastAPI()

# инициализация статики
app.mount("/static", StaticFiles(directory="public", html=True))

# загрузка CNN
PATH_CNN_WEIGHTS = "./ml_models/filter/alexnet/alexnet_waights.pth"
model_cnn = BaseLine(path_model_weight=PATH_CNN_WEIGHTS)


@app.get("/")
def root():
    return JSONResponse(content={"message": "API в котором расположена CNN для оценки filter."}, status_code=status.HTTP_200_OK)

@app.post("/send/img/")
async def create_upload_file(file: UploadFile):
    """Загрузка файла с нейронкой"""

    img = file.file

    # делаем предсказание и ловим исключения в случае ошибки модели
    try:
        img = Image.open(img)
        prediction = model_cnn.predict_file_by_loaded_binary(opened_img=img)
    except Exception as e:
        return JSONResponse(str(e), status_code=status.HTTP_400_BAD_REQUEST)

    example = {
        "filter": {"type": prediction},
    }

    return JSONResponse(example, status_code=status.HTTP_200_OK)

@app.post("/send/url/")
async def create_upload_file(url: str = Body(embed=True)):
    """Загрузка файла с нейронкой"""

    # делаем предсказание и ловим исключения в случае ошибки модели
    try:
        prediction = model_cnn.predict_file_by_url(url=url)
    except Exception as e:
        return JSONResponse(str(e), status_code=status.HTTP_400_BAD_REQUEST)

    example = {
        "filter": {"type": prediction},
    }

    return JSONResponse(example, status_code=status.HTTP_200_OK)

###################################


class MlRequest(BaseModel):
    bad_to_eat: int
    little_energy: int
    rash: int
    liquid_poop: int


PATH_CATBOOST_WEIGHTS = "./ml_models/poll/catboost/parasites_catboost.cbm"
model_catboost = PollBaseline(path_model_weight=PATH_CATBOOST_WEIGHTS)


@app.post("/send/poll/") # , response_model=MlRequest
async def create_upload_file(parameters: MlRequest):
    """Загрузка файла"""

    prediction = model_catboost.predict(**parameters.dict())
    return {"prediction": prediction}

