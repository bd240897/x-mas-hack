# torch
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torchvision import datasets, models, transforms

# python
import os
import json
from pathlib import Path
from os.path import basename
import requests
from io import BytesIO

# ml-modules
import numpy as np

# img
from PIL import Image

# turn off warnings
import warnings

warnings.filterwarnings('ignore')

class BaseLine:
    """Фильтр. Получает фото jpg и дает предсказание 1го из 2х классов"""

    ALLOWED_FILE_EXTENSION = ['JPG', "JPEG"]

    def __init__(self, path_model_weight: str):
        """
        :param path_model_weight: путь до весов модели
        """
        self.path_model_weight = path_model_weight

        self._get_map_labels()
        self._get_transformer()
        self._get_model()
        self._load_model_weights()

    def _get_map_labels(self):
        """Декодированием меток"""

        self.map_labels = ['other', 'poop']

    def _get_transformer(self):
        """Трансформация входных данных"""

        self.data_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(244),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def _get_model(self):
        """Создание модели"""

        model_extractor = models.alexnet(weights=False)
        model_extractor.classifier = nn.Linear(9216, 2)
        self.model = model_extractor

    def _load_model_weights(self):
        """Загрузка весов модели"""

        self.model.load_state_dict(torch.load(self.path_model_weight))

    # ПРОВЕРКИ

    def _check_img_extension_by_url(self, url: str):
        """Проверка расширения по урлу"""

        img_extension = url.rsplit('/', 1)[1].rsplit('.', 1)[1]
        if not img_extension.upper() in self.ALLOWED_FILE_EXTENSION:
            raise Exception("Расширение файла не .jpg")

    def _check_img_extension_by_path(self, img: Image):
        """Проверка расширения с помощью Pillow"""

        if not str(img.format).upper() in self.ALLOWED_FILE_EXTENSION:
            raise Exception("Расширение файла не .jpg")

    def _load_img_by_url(self, url: str):
        """Открытие изображения и его траснформация по url"""

        # проверка расширения файла
        self._check_img_extension_by_url(url)

        # загрузка изображения из инета
        response = requests.get(url)
        content = BytesIO(response.content)

        # Открытие изображения и его траснформация
        opened_img = Image.open(content)

        return opened_img

    def _load_img_by_path(self, img_path: str):
        """Открытие изображения и его траснформация по path"""

        # Открытие изображения и его траснформация
        opened_img = Image.open(img_path)

        # проверка расширения файла
        self._check_img_extension_by_path(opened_img)

        return opened_img

    def _predict_block(self, opened_img: Image):
        """
        Блок для предсказания

        :param opened_img: откратая картинка с помощью Image.open(...) из _load_file_by_path или _load_file_by_url
        :return: предсказанный класс из self.get_map_labels()
        """

        # трансформация данных
        transformed_img = self.data_transforms(opened_img)

        # делаем предсказание
        with torch.no_grad():
            self.model.eval()
            logit = self.model(transformed_img.unsqueeze(0))
            probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
            id = np.argmax(probs)
            predicted_class = self.map_labels[id]
        return predicted_class

    def predict_file_by_url(self, url: str):
        """Предсказать по url"""

        opened_img = self._load_img_by_url(url)
        return self._predict_block(opened_img)

    def predict_file_by_path(self, img_path: str):
        """Предсказать по path"""

        opened_img = self._load_img_by_path(img_path)
        return self._predict_block(opened_img)

    def predict_file_by_loaded_binary(self, opened_img: Image):
        """Предсказать по открытому бинарному файлу"""

        return self._predict_block(opened_img)

if __name__ == '__main__':
    """
    Порядок запуска функций
    url - на входи принимает url картинки
    path - на вход принимает картинку
    loaded_binary - на вход принимает открытую бинарную картинку, например Image.open(...)
    """

    # КАТАЛОГИ
    BASE_DIR = r"C:\Games\Python_works\x-mas-hack\kaspersky_hack\learn_fast_api"
    FOLDER_NAME = 'ml_models'
    PATH_MODEL_WEIGHTS = os.path.join(BASE_DIR, FOLDER_NAME, "ml_alexnet", 'alexnet_waights.pth')

    # КАРТИНКА
    IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
    IMG_PATH = os.path.join(BASE_DIR, FOLDER_NAME, "static", "1.jpg")

    type_input = "path"

    model = BaseLine(path_model_weight=PATH_MODEL_WEIGHTS)

    if type_input == "url":
        prediction = model.predict_file_by_url(url=IMG_URL)
    elif type_input == "path":
        prediction = model.predict_file_by_path(img_path=IMG_PATH)
    elif type_input == "loaded_binary":
        opened_img = Image.open(IMG_PATH)
        prediction = model.predict_file_by_loaded_binary(opened_img=opened_img)
    else:
        prediction = "Ошибка в коде"
    print(prediction)



    #
    # im = Image.open(IMG_PATH)
    # print(im.verify())
    # print(im.format)
    # # im.show()
    # # im.close()
