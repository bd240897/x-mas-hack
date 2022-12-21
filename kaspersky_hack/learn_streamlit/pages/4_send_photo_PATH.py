import io
from io import BytesIO
from PIL import Image
import streamlit as st
import requests

from ml_models.ml_alexnet.BaselineClass import BaseLine


def image_to_byte_array(image: Image) -> bytes:
    """Переводит картинку pillow image в байты"""

    # BytesIO is a fake file stored in memory
    imgByteArr = io.BytesIO()
    # image.save expects a file as a argument, passing a bytes io ins
    image.save(imgByteArr, format=image.format)
    # Turn the BytesIO object back into a bytes object
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


uploaded_file = st.file_uploader("Choose a image file", type="jpg")

if uploaded_file is not None:
    # Convert the file to an opencv image.
    # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    # opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    st.image(uploaded_file.read(), channels="BGR")

    send_button = st.button("Send photo")

    if send_button:
        PATH_MODEL_WEIGHTS = "./ml_models/ml_alexnet/alexnet_waights.pth"
        model = BaseLine(path_model_weight=PATH_MODEL_WEIGHTS)
        opened_img = Image.open(uploaded_file)
        prediction = model.predict_file_by_loaded_binary(opened_img=opened_img)
        st.write(prediction)






