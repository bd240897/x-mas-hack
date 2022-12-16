import streamlit as st
import os

st.title('Страница опроса :blue[colors] :sunglasses:')

st.write('Пожалуйста пройдите опрос')

# КОНСТАНТЫ
# список ответов
LIST_WEIGHTS = []
IS_POLL_SHOW = True  # виден ли опрос
# st.session_state['IS_POLL_SHOW'] = 'True' # виден ли опрос

st.write(":blue[colors]")

# st.button('click', on_click=send_poll)
print(st.session_state['IS_POLL_SHOW'])
if st.session_state['IS_POLL_SHOW']:
    poll_questions()


try:
    st.session_state['IS_POLL_SHOW']
except KeyError:
    st.session_state['IS_POLL_SHOW'] = True

def calculate_user_status(answers: list):
    """Получает инвест профиль пользователя"""
    """Заглушка"""

    answers_sum = sum(answers)

    if answers_sum < 2:
        user_status = "Консервативный"
    elif answers_sum < 4:
        user_status = "Умеренный"
    else:
        user_status = "Рискованный"
    return user_status


# on click - callback on_change
def send_poll():
    """Отправить опрос"""

    st.session_state['IS_POLL_SHOW'] = False
    user_status = calculate_user_status(answers_list)
    st.session_state['user_status'] = user_status
    st.write(f":blue[{user_status}]")


def poll_questions():
    """Генерация опроса"""

    # ОПРОС
    answers_task_1 = ['до 1 года', 'до 3-х лет', 'до 5-ти лет', 'до 10-ти лет']
    labels_task_1 = range(4)
    task_1 = st.radio(
        label=f"На какой срок вы планируете инвестировать?",
        options=labels_task_1,
        format_func=lambda i: answers_task_1[i]
    )
    answers_list.append(task_1)

    answers_task_2 = ('переживаю', 'не переживаю')
    labels_task_2 = range(2)
    task_2 = st.radio(
        label="Как вы относитесь к риску?",
        options=labels_task_2,
        format_func=lambda i: answers_task_2[i]
    )
    answers_list.append(task_2)

    answers_task_3 = ('переживаю', 'не переживаю')
    labels_task_3 = range(2)
    task_3 = st.radio(
        label="Еще вопрос номер 3?",
        options=labels_task_3,
        format_func=lambda i: answers_task_3[i]
    )
    answers_list.append(task_3)

    answers_task_4 = ['до 1 года', 'до 3-х лет', 'до 5-ти лет', 'до 10-ти лет']
    labels_task_4 = range(4)
    task_4 = st.radio(
        label="Еще вопрос номер 3?",
        options=labels_task_4,
        format_func=lambda i: answers_task_4[i]
    )
    answers_list.append(task_4)

    # st.write(task_4)
    increment = st.button('Отправить', on_click=send_poll)

    if increment:
        st.write('Итоги опроса:')
        st.text(f"1 -{task_1}, \n"
                f"2 -{task_2}, \n"
                f"3 -{task_3}. \n"
                f"4 -{task_4}. \n")





# input
increment_value = st.number_input('Enter a value', value=0, step=1)

# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn\'t select comedy.")

btn = st.multiselect(
    "Some text", [2, 4, 6, 8, 10], format_func=lambda x: "option " + str(x)
)