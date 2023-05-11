import random
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import ChatPool

router = APIRouter()


def get_user():
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(16):
        random_str += base_str[random.randint(0, length)]
    return random_str


@router.get("/chat/prechat")
async def prechat(age: int, work: str, interest: str):
    id = get_user()
    feature = f"""我是{age}岁的{work}，我喜欢{interest}，想和你聊天，可以的话请回复我：“你好。”。"""
    ChatPool.prechat(id, feature)
    return JSONResponse({
        "code": 200,
        "data": {
            "id": id,
            "msg": "你好。"
        }
    })


@router.get("/chat/chat")
async def chat(id: str, msg: str):
    answer = ChatPool.chat(id, msg)
    return JSONResponse({
        "code": 200,
        "data": {
            "id": id,
            "message": answer
        }
    })
