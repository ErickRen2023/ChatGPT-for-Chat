from fastapi import FastAPI
import requests as r
from fastapi.middleware.cors import CORSMiddleware
from routers import router

app = FastAPI()

app.docs_url = None
app.redoc_url = None

origins = [
    "ai.9998k.cn",
    '127.0.0.1',
    'null',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

apikeys_load = list()
# noinspection PyBroadException
try:
    with open("settings/apikeys.txt", "r") as f:
        apikeys_str = f.read()
        apikeys_load = apikeys_str.split("\n")
except Exception:
    print("An error in loading apikeys_load.")
else:
    print("Load apikeys_load successfully.")

apikeys = list()
print("Checking apikeys_load....")
url = "https://api.openai.com/v1/chat/completions"
for i in apikeys_load:
    authorization = "Bearer " + i
    headers = {
        "Content-Type": "application/json",
        "Authorization": authorization
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello!"}]
    }
    response = r.post(url, json=data, headers=headers)
    if "error" in response.text:
        print("Can't use apikeys_load:[" + i + "] !")
    elif "content" in response.text:
        print("Can use apikeys_load:[" + i + "].")
        apikeys.append(authorization)
    else:
        print("Unknown Error!")

app.include_router(router.router)





