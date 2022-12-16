import streamlit as st
from logic.poll import calculate_user_status, poll_questions
import os

st.title('Страница опроса :blue[colors] :sunglasses:')

try:
    a = st.session_state['IS_POLL_SHOW']
except:
    st.session_state['IS_POLL_SHOW'] = 'True'


# on click - callback on_change
def click():
    st.session_state['IS_POLL_SHOW'] = False
    user_status = calculate_user_status(st.session_state.answers_list)
    st.session_state['user_status'] = user_status


if st.session_state['IS_POLL_SHOW']:
    st.write('Пожалуйста пройдите опрос')
    poll_questions()
    button_1 = st.button('Отравить', on_click=click)
else:
    st.header(f"Ваш статус:")
    st.header(f":blue[{st.session_state.user_status}]")










# def send_poll():
#     """Отправить опрос"""
#
#     st.session_state['IS_POLL_SHOW'] = False
#     user_status = calculate_user_status(answers_list)
#     st.session_state['user_status'] = user_status
#     st.write(f":blue[{user_status}]")




# input
increment_value = st.number_input('Enter a value', value=0, step=1)

# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn\'t select comedy.")

btn = st.multiselect(
    "Some text", [2, 4, 6, 8, 10], format_func=lambda x: "option " + str(x)
)
