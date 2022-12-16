import streamlit as st


def calculate_user_status(answers: list):
    """Получает инвест профиль пользователя"""
    """Заглушка"""

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

def send_poll():
    """Отправить опрос"""
    st.session_state['IS_POLL_SHOW'] = False

def poll_questions():
    """Генерация опроса"""

    answers_list = []
    answers_weight_list = []

    # ОПРОС
    answers_task_1 = ['до 1 года', 'до 3-х лет', 'до 5-ти лет', 'до 10-ти лет']
    weight_task_1 = [1, 2, 3, 4]
    labels_task_1 = range(4)
    task_1 = st.radio(
        label=f"На какой срок вы планируете инвестировать?",
        options=labels_task_1,
        format_func=lambda i: answers_task_1[i]
    )
    answers_list.append(task_1)
    answers_weight_list.append(weight_task_1[task_1])

    answers_task_2 = ('переживаю', 'нейтральной', 'не переживаю')
    weight_task_2 = [1, 2, 3]
    labels_task_2 = range(3)
    task_2 = st.radio(
        label="Как вы относитесь к кратковременным просадкам в вашем портфеле?",
        options=labels_task_2,
        format_func=lambda i: answers_task_2[i]
    )
    answers_list.append(task_2)
    answers_weight_list.append(weight_task_2[task_2])

    answers_task_3 = ('18-27 лет', '27-45 лет', '45-65 лет', '65 лет')
    weight_task_3 = [4, 3, 2, 1]
    labels_task_3 = range(4)
    task_3 = st.radio(
        label="К какой возрастной группу вы относитесь?",
        options=labels_task_3,
        format_func=lambda i: answers_task_3[i]
    )
    answers_list.append(task_3)
    answers_weight_list.append(weight_task_3[task_3])

    answers_task_4 = ['не имею опыта', 'меньше года', 'больше года']
    weight_task_4 = [1, 2, 3]
    labels_task_4 = range(3)
    task_4 = st.radio(
        label="Какой опыт вы имеете в инвестировании?",
        options=labels_task_4,
        format_func=lambda i: answers_task_4[i]
    )
    answers_list.append(task_4)
    answers_weight_list.append(weight_task_4[task_4])

    # increment = st.button('Отправить')
    #
    # if increment:
    #     st.write('Итоги опроса:')
    #     st.text(f"1 -{task_1}, \n"
    #             f"2 -{task_2}, \n"
    #             f"3 -{task_3}. \n"
    #             f"4 -{task_4}. \n")

    st.session_state['answers_list'] = answers_list
    st.session_state['answers_weight_list'] = answers_weight_list
