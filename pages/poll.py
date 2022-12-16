import streamlit as st
from logic.poll import calculate_user_status, poll_questions
import os

st.title('Это страница опроса :sunglasses:')

try:
    a = st.session_state['IS_POLL_SHOW']
except:
    st.session_state['IS_POLL_SHOW'] = 'True'


# on click - callback on_change
def send_poll():
    st.session_state['IS_POLL_SHOW'] = False
    user_status = calculate_user_status(st.session_state.answers_list)
    st.session_state['user_status'] = user_status


def go_to_portfolio():
    pass

if st.session_state['IS_POLL_SHOW']:
    st.write('Пожалуйста пройдите опрос')
    poll_questions()
    button_1 = st.button('Отравить', on_click=send_poll)
else:
    st.header(f"Ваш статус:")
    st.header(f":blue[{st.session_state.user_status}]")
    button_1 = st.button('Отравить', on_click=go_to_portfolio)

