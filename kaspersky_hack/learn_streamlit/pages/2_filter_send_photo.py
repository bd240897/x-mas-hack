import io
from io import BytesIO
from PIL import Image
import streamlit as st
import requests

from ml_models.filter.alexnet.FilterBaseline import FilterBaseline


def image_to_byte_array(image: Image) -> bytes:
    """Переводит картинку pillow image в байты"""

    # BytesIO is a fake file stored in memory
    imgByteArr = io.BytesIO()
    # image.save expects a file as a argument, passing a bytes io ins
    image.save(imgByteArr, format=image.format)
    # Turn the BytesIO object back into a bytes object
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


# КОНСТАНТЫ
IMG_URL = r"https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
BACKEND_SEND_IMG_URL = "http://127.0.0.1:8000/send/img/"
BACKEND_SEND_URL_URL = "http://127.0.0.1:8000/send/url/"
PATH_MODEL_WEIGHTS = "./ml_models/filter/alexnet/alexnet_waights.pth"

st.write(f"## Выберите тип отправки фотографии")

st.selectbox(
    'Какой тип отправки фото вы ходите?',
    ('None', "send_url", "send_file", "send_url_local", "send_file_local"), key="type_input")

st.markdown("""__Описание__: 
- __send_url__ - url фотографии отправляется на FastApi
- __send_file__ - файл фотографии *.jpg отправляется на FastApi
- __send_url_local__ - url фотографии отправляется на локальную версию CNN
- __send_file_local__ - файл фотографии *.jpg отправляется на локальную версию CNN
""")


if st.session_state.type_input == "send_url":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ url фотографии отправляется на FastApi")

    st.text_input(
        label="Введите url картинки",
        value=IMG_URL,
        key="send_url_input")

    if st.session_state.send_url_input:
        # открытие фотографии
        st.image(st.session_state.send_url_input)
        # кнопка отправки
        st.button("Отправить", key="send_url_button")
        # логика отправки

        if st.session_state.send_url_button:
            # img = Image.open(uploaded_file)

            response = requests.post(BACKEND_SEND_URL_URL, json={"url": IMG_URL})
            # логика отправки
            st.write(response.status_code)
            st.markdown("### Найденные болезни:")
            if response.status_code == requests.codes.ok: #200
                st.write(response.json())
                # for item in response.json():
                #     name = item.get("name")
                #     st.markdown(f"- {name}")


elif st.session_state.type_input == "send_file":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ файл фотографии *.jpg отправляется на FastApi")

    uploaded_file = st.file_uploader("Choose a image file", type="jpg")

    if uploaded_file is not None:
        # открытие фотографии
        st.image(uploaded_file.read(), channels="BGR")
        # кнопка отправки
        send_button = st.button("Отправить", key="send_file_button")
        # логика отправки

        if st.session_state.send_file_button:
            img = Image.open(uploaded_file)
            response = requests.post(BACKEND_SEND_IMG_URL,
                                     files={"file": ('1.jpg', image_to_byte_array(img), 'image/jpeg')})
            # логика отправки
            st.write(response.status_code)
            st.markdown("### Найденные болезни:")
            if response.status_code == 200:
                st.write(response.json())
                # for item in response.json():
                #     name = item.get("name")
                #     st.markdown(f"- {name}")

elif st.session_state.type_input == "send_url_local":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ url фотографии отправляется на локальную версию CNN")

    st.text_input(
        label="Введите url картинки",
        value=IMG_URL,
        key="send_url_input_local")

    if st.session_state.send_url_input_local:
        # открытие фотографии
        st.image(st.session_state.send_url_input_local)
        # кнопка отправки
        send_button = st.button("Отправить", key="send_url_local_button")
        # логика отправки

        if st.session_state.send_url_local_button:
            model = FilterBaseline(path_model_weight=PATH_MODEL_WEIGHTS)
            prediction = model.predict_file_by_url(url=st.session_state.send_url_input_local)
            st.write(prediction)


elif st.session_state.type_input == "send_file_local":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
    st.markdown(f"__Описание:__ файл фотографии *.jpg отправляется на локальную версию CNN")

    uploaded_file_local = st.file_uploader("Choose a image file", type="jpg")

    if uploaded_file_local is not None:
        # открытие фотографии
        st.image(uploaded_file_local.read(), channels="BGR")
        # кнопка отправки
        send_button = st.button("Отправить", key="send_url_file_button")
        # логика отправки
        if st.session_state.send_url_file_button:
            model = FilterBaseline(path_model_weight=PATH_MODEL_WEIGHTS)
            opened_img = Image.open(uploaded_file_local)
            prediction = model.predict_file_by_loaded_binary(opened_img=opened_img)
            st.write(prediction)

elif st.session_state.type_input == "None":
    st.markdown(f"### Тип отправки: {st.session_state.type_input}")
