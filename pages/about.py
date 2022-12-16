import streamlit as st

st.title('Это просто страница с мусором')


# доп информация о странице
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('Страница about :blue[colors] :sunglasses:')

form = st.form("my_form")
form.slider("Inside the form")

# Now add a submit button to the form:
w4 = form.form_submit_button("Submit")

print(w4)

if w4:
    form2 = st.form("my_form2")
    form2.slider("Inside the form")
    form2.form_submit_button("Submit")
