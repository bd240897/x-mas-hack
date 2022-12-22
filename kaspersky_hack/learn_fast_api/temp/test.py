import requests

IMG_URL = r"https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
BACKEND_SEND_IMG_URL = "http://127.0.0.1:8000/send/img/"
BACKEND_SEND_URL_URL = "http://127.0.0.1:8000/send/url/"

# response = requests.post(BACKEND_SEND_URL_URL, json={"url": IMG_URL})
# print(response.status_code)
# print(response.text)

print(requests.codes.ok)