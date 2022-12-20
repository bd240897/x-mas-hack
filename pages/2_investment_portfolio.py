import streamlit as st
import matplotlib.pyplot as plt

try:
    a = st.session_state['user_status']
except:
    st.session_state['user_status'] = 'Консервативный'


def portfolio_1(type_info: str):
    if type_info == 'graph':
        st.write("Консервативный портфель")
        labels = ['Акции',
                  'Облигации',
                  ]

        values = [10,
                  90,
                  ]
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels)
        ax1.axis('equal')
        plt.show()
        st.pyplot(fig1)
    elif type_info == "recommendation":
        st.write("- инвестировать регулярно")
        st.write("- покупать облигации, они являются наименее рискованным инструментом")



def portfolio_2(type_info:str):
    if type_info == 'graph':
        st.write("Сбалансированный портфель")
        labels = ['Акции',
                  'Облигации',
                  ]

        values = [30,
                  70,
                  ]
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels)
        ax1.axis('equal')
        plt.show()
        st.pyplot(fig1)
    elif type_info == "recommendation":
        st.write("- инвестировать регулярно")
        st.write("- покупать акции и облигации в заданном соотношении")

def portfolio_3(type_info: str):
    if type_info == 'graph':
        st.write("Рискованный портфель")
        labels = ['Акции',
                  'Облигации',
                  ]

        values = [50,
                  50,
                  ]
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels)
        ax1.axis('equal')
        plt.show()
        st.pyplot(fig1)
    elif type_info == "recommendation":
        st.write("- инвестировать регулярно")
        st.write("- покупать акции и облигации в заданном соотношении")

# st.header("Section 2")
# st.header("Section 3")
# st.markdown("[Section 1](#section-1)")


col1, col2, = st.columns(2)

with col1:
    st.header("Рекомендации")
    if st.session_state.user_status == "Консервативный":
        portfolio_1("recommendation")
    elif st.session_state.user_status == "Умеренный":
        portfolio_2("recommendation")
    elif st.session_state.user_status == "Рискованный":
        portfolio_3("recommendation")

with col2:
    st.header("Тип рекомендуемого портфеля")
    if st.session_state.user_status == "Консервативный":
        portfolio_1("graph")
    elif st.session_state.user_status == "Умеренный":
        portfolio_2("graph")
    elif st.session_state.user_status == "Рискованный":
        portfolio_3("graph")
    st.write("* Соотношение акций и облигаций")

