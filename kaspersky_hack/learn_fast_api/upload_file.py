from enum import Enum
from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """Загрузка файла"""

    img = file.file
    try:
        im = Image.open(img)
        im.verify()  # I perform also verify, don't know if he sees other types o defects
        im.close()  # reload is necessary in my case
    except Exception as e:
        print(e)
        return "Ошибка чтения файла"
    return {"filename": file.filename}