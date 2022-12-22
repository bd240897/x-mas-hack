import warnings
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
warnings.filterwarnings('ignore')

class PollBaseline:
    """Фильтр. Получает фото jpg и дает предсказание 1го из 2х классов"""

    def __init__(self, path_model_weight: str):
        """
        :param path_model_weight: путь до весов модели
        """
        self.path_model_weight = path_model_weight

        self._get_map_labels()
        self._get_model()
        self._load_model_weights()

    def _get_map_labels(self):
        """Декодированием меток"""

        self.map_labels = ['healthy', 'parasites']

    def _get_model(self):
        """Создание модели"""

        self.model = CatBoostClassifier()

    def _load_model_weights(self):
        """Загрузка весов модели"""

        self.model.load_model(self.path_model_weight, format='cbm')

    def predict(self, bad_to_eat, little_energy, rash, liquid_poop):
        """Сделать предсказание"""

        df = pd.DataFrame([[bad_to_eat, little_energy, rash, liquid_poop]],
                          columns=["bad_to_eat", "little_energy", "rash", "liquid_poop"])
        preds_proba = self.model.predict_proba(df).tolist()[0]
        max_index = np.argmax(preds_proba)
        return self.map_labels[max_index]


if __name__ == '__main__':
    """Порядок запуска функций"""

    # КАТАЛОГИ
    PATH_POLL_WEIGHTS = "./parasites_catboost.cbm"

    model = PollBaseLine(path_model_weight=PATH_POLL_WEIGHTS)
    poll_answers = {
        "bad_to_eat": 1,
        "little_energy": 1,
        "rash": 1,
        "liquid_poop": 1
    }
    prediction = model.predict(**poll_answers)
    print(prediction)

