import json

import requests
import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor, CatBoostClassifier
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# Set Page Layout
st.set_page_config(layout='wide')

model = CatBoostClassifier()
model.load_model('static/models/parasites_catboost.cbm', format='cbm')


def predict(bad_to_eat, little_energy, rash, liquid_poop):
    df = pd.DataFrame([[bad_to_eat, little_energy, rash, liquid_poop]],
                      columns=["bad_to_eat", "little_energy", "rash", "liquid_poop"])
    prediction = model.predict(df)

    preds_class = model.predict(df)
    # Get predicted probabilities for each class
    preds_proba = model.predict_proba(df)
    # Get predicted RawFormulaVal
    preds_raw = model.predict(df, prediction_type='RawFormulaVal')
    return preds_class, preds_proba, preds_raw


st.title('Страница опроса:')
st.image(
    """https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Опрос на наличие паразитов:')

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

#
# carat = st.number_input('Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)
#
# cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
#
# color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
#
# clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
#
# depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
#
# table = st.number_input('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)
#
# x = st.number_input('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
#
# y = st.number_input('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
#
# z = st.number_input('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)

if st.button('Predict Price'):
    preds_class, preds_proba, preds_raw = predict(bad_to_eat, little_energy, rash, liquid_poop)
    # st.success(prediction)
    st.text(f"""{preds_class}
    {preds_proba}
    {preds_raw}
    """)

