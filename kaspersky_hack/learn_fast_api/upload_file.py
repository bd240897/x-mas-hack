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

from .ml_models.ml_alexnet.BaselineClass import BaseLine

app = FastAPI()
app.mount("/static", StaticFiles(directory="public", html=True))

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """Загрузка файла тест"""

    img = file.file
    try:
        im = Image.open(img)
        im.verify()  # I perform also verify, don't know if he sees other types o defects
        im.close()  # reload is necessary in my case
    except Exception as e:
        print(e)
        return "Ошибка чтения файла"
    return {"filename": file.filename}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    """Загрузка файла с нейронкой"""

    img = file.file

    # предсказание нейронки
    model = BaseLine()

    # делаем предсказание и ловим исключения в случае ошибки модели
    try:
        prediction = model.predict_file(url=url)
    except Exception as e:
        return JSONResponse(str(e), status_code=status.HTTP_400_BAD_REQUEST)

    example = {
        "filter": {"type": prediction},
    }

    return JSONResponse(example, status_code=status.HTTP_200_OK)


security = HTTPBasic()
def authorize(credentials: HTTPBasicCredentials = Depends(security)):
    is_user_ok = secrets.compare_digest(credentials.username, 'amid') #os.getenv('LOGIN')
    is_pass_ok = secrets.compare_digest(credentials.password, '1') #os.getenv('PASSWORD')

    if not (is_user_ok and is_pass_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password.',
            headers={'WWW-Authenticate': 'Basic'},
        )

@app.get("/about/", dependencies=[Depends(authorize)])
def root():
    return JSONResponse(content={"message": "API в котором расположена найронка для оценки фотографии"}, status_code=status.HTTP_200_OK)

@app.get("/logo/")
def root():
    return FileResponse("public/1.jpg",) # filename="1.jpg",media_type="application/octet-stream"

@app.post("/hello")
#def hello(name = Body(embed=True)):
def hello(data = Body()):
    print(data["name"])
    # name = data["name"]
    # age = data["age"]
    # return {"message": f"{name}, ваш возраст - {age}"}
    return JSONResponse(content='', status_code=status.HTTP_200_OK)

@app.get("/cookie/")
def root(response: Response):
    now = datetime.now()    # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=str(now))
    return  {"message": "куки установлены"}


@app.post("/postdata")
def postdata(username = Form(), age=Form()):
    return {"name": username, "age": age}

@dataclass
class Person(BaseModel):
    username: str = Form(...)
    age: str = Form(...)

@app.post("/postdata2")
def postdata(item: Person = Depends()):
    return item


"""
функции?
отдать иконку
рассказать кто я
получить фотку и предсказать
"""
