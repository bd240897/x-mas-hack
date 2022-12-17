import streamlit as st
import os

st.title('Рекомендационная система для подбора портфеля')



st.write('### Идея решения')
st.text("""
1) Пользователь проходит опрос.
2) Но основании опроса ему назначается тип риска (например консервативный). 
3) Наша "рекомендационная система" предлагает ему на выбор один из готовых портфелей исходя из его профиля риска. А также рекомендации как вести этот портфель дальше по месяцам ( например, чтоб соотношение акций и облигаций не изменялось)
""")

col1, col2, = st.columns(2)

with col1:
    st.write('### Масштабирование')
    st.write('- улучшение опроса')
    st.write('- добавление больше заготовленных портфелей')
    st.write('- добавление криптовалюты')

with col2:
    st.write('### Достоинства')
    st.write('- простота')
    st.write('- доступность')
    st.write('- автоматизация')
    st.write('- масштабируемость')