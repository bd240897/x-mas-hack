import streamlit as st
import matplotlib.pyplot as plt


try:
    a = st.session_state['user_status']
except:
    st.session_state['user_status'] = 'Консервативный'

def porfolio_1():
    st.header("Консервативный портфель")
    labels = ['Акции',
              'Облигации',
              ]

    values = [90,
              10,
              ]
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels)
    ax1.axis('equal')
    plt.show()
    st.pyplot(fig1)


def porfolio_2():
    st.header("Сбалансированный портфель")
    labels = ['Акции',
              'Облигации',
              ]

    values = [70,
              30,
              ]
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels)
    ax1.axis('equal')
    plt.show()
    st.pyplot(fig1)

def porfolio_3():
    st.header("Рискованный портфель")
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



# st.header("Section 2")
#
# st.header("Section 3")
#
# st.markdown("[Section 1](#section-1)")


# st.experimental_set_query_params(
#     show_map=True,
#     selected=["asia", "america"],
# )

if st.session_state.user_status == "Консервативный":
    porfolio_1()
elif st.session_state.user_status == "Умеренный":
    porfolio_2()
elif st.session_state.user_status == "Рискованный":
    porfolio_3()







def make_clickable(link):
    text = link.split('=')[0]
    return f'<a target="_blank" href="/">1234</a>'


st.write(f'<a target="_blank" href="/">1234</a>', unsafe_allow_html=True)

st.button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel')
