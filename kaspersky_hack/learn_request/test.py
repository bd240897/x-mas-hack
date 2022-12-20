import base64
import json
from io import BytesIO
import requests

URL = "http://127.0.0.1:8000/api/v2/request/photo/quick/"
FILE = "1.jpg"
with open(FILE, "rb") as f:
    data = f.read()
    r = requests.post(URL, files={"file": ('1.jpg', data, 'image/jpeg')})
    print(r.json())
