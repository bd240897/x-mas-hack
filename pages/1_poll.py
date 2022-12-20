import streamlit as st
# from logic.poll import calculate_user_status
import os
import json

# НАЧАЛЬНЫЕ УСЛОВИЯ

# первоначальная инициализация
if 'is_poll_show' not in st.session_state:
    st.session_state['is_poll_show'] = True

# ИСПОЛЬЩУЕМЫЕ ФУНКЦИИ

def send_poll():
    """Обратный вызов для кнопки отравить опрос"""

    st.session_state['is_poll_show'] = False
    user_status = calculate_user_status(st.session_state.answers_weight_list)
    st.session_state['user_status'] = user_status


def show_poll():
    """Обратный вызова для кнопки показать опрос"""

    st.session_state['is_poll_show'] = True


def go_to_portfolio():
    """Обратный вызова для кнопки перейти к портфолио"""

    pass


def poll_questions():
    """Генерация опроса"""

    answers_list = []
    answers_weight_list = []

    with open('questions.json', encoding='utf-8') as f_in:
        questions = json.load(f_in)

    def poll_item(question: str, answers: list, weight: list):
        """Один элемент опроса"""

        labels_poll = range(len(answers))  # range(4)

        user_answer = st.radio(
            label=question,
            options=labels_poll,
            format_func=lambda i: answers[i]
        )
        answers_list.append(user_answer)
        answers_weight_list.append(weight[user_answer])

    for item in questions:
        poll_item(item["question"], item["answers"], item["weight_poll"])

    st.session_state['answers_list'] = answers_list
    st.session_state['answers_weight_list'] = answers_weight_list


def calculate_user_status(answers: list):
    """Получает инвест профиль пользователя"""
    """
    max - 16
    min 4
    Пороги
    Консервативный  <8
    Умеренный <12
    Рискованный >=13
    """

    answers_sum = sum(answers)

    if answers_sum < 8:
        user_status = "Консервативный"
    elif answers_sum < 12:
        user_status = "Умеренный"
    else:
        user_status = "Рискованный"
    return user_status

# КОД СТРАНИЦЫ

# заголовок
st.title('Это страница опроса :sunglasses:')

if st.session_state.is_poll_show:
    st.write('Пожалуйста пройдите опрос')
    poll_questions()
    st.button('Отравить', on_click=send_poll)
else:
    st.header(f"Ваш статус:")
    st.header(f":blue[{st.session_state.user_status}]")
    st.button('Перейти к портфелю', on_click=go_to_portfolio)
    st.button('Пройти опрос еще раз', on_click=show_poll)

# st.button('session_state', on_click=send_poll, key='my_button')
# st.markdown(f"""
# #### {st.session_state}
# """)
