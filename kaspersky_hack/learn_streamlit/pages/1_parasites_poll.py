import json
import requests
import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor, CatBoostClassifier
import ssl
from ml_models.poll.catboost.PollBaseline import PollBaseline

# КОНСТАНТЫ
PATH_MODEL_WEIGHTS = "./ml_models/poll/catboost/parasites_catboost.cbm"
BACKEND_SEND_POLL_URL = "http://127.0.0.1:8000/send/poll/"

# МОДЕЛЬ
model_catboost = PollBaseline(path_model_weight=PATH_MODEL_WEIGHTS)

st.selectbox(
    'Какой тип отправки фото вы ходите?',
    ('None', "send_poll", "send_poll_local"), key="type_input")

st.markdown("""__Описание__: 
- __send_poll__ - опрос отправляется на FastApi
- __send_poll_local__ - опрос отправляется на локальную версию Classifier
""")

st.title('Страница опроса:')
st.markdown('### Опрос на наличие паразитов:')

def poll_parasites_questions():
    answers = ["да", "нет"]
    bad_to_eat = st.selectbox(
        label='Ваша собака плохо ест?',
        options=[0, 1],
        format_func=lambda i: answers[i]
    )

    little_energy = st.selectbox(
        label='У вашей собаки жидкий стул?',
        options=[0, 1],
        format_func=lambda i: answers[i]
    )
    rash = st.selectbox(
        label='У собаки есть сыпь?',
        options=[0, 1],
        format_func=lambda i: answers[i]
    )
    liquid_poop = st.selectbox(
        label='Ваша собака малоэнерегичная?',
        options=[0, 1],
        format_func=lambda i: answers[i]
    )

    poll_answers = {
        "bad_to_eat": bad_to_eat,
        "little_energy": little_energy,
        "rash": rash,
        "liquid_poop": liquid_poop
    }

    return poll_answers


if st.session_state.type_input == "send_poll":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ опрос отправляется на FastApi")

    poll_answers = poll_parasites_questions()

    if st.button('Отправить'):
        response = requests.post(url=BACKEND_SEND_POLL_URL, data=json.dumps(poll_answers))
        st.write(response.json().get("prediction"))

elif st.session_state.type_input == "send_poll_local":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ опрос отправляется на локальную версию Classifier")

    poll_answers = poll_parasites_questions()

    if st.button('Отправить'):
        prediction = model_catboost.predict(**poll_answers)
        # st.success(prediction)
        st.text(f"""{prediction}""")
