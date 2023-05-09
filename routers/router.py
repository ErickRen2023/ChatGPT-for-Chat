import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests as r
import main

router = APIRouter()



url = "https://api.openai.com/v1/chat/completions"


def get_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": main.apikeys[random.randint(0, len(main.apikeys) - 1)]
    }
    return headers


def get_user():
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(16):
        random_str += base_str[random.randint(0, length)]
    return random_str


@router.get("/chat/prechat")
async def prechat(age: int, work: str, interest: str):
    user = get_user()
    prechat_content = f"""我是{age}岁的{work}，我喜欢{interest}，想和你聊天，可以的话请回复我：“你好。”"""
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prechat_content}],
        "user": get_user()
    }
    response = r.post(url, json=data, headers=get_headers())
    if "content" not in response.text:
        return JSONResponse(response.text)
    else:
        return JSONResponse({
            "code": 400,
            "message": "Unknown Error!"
        })

