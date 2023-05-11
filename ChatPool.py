import random
import requests as r
import main
import json

url = "https://api.openai.com/v1/chat/completions"


def get_headers() -> dict:
    headers = {
        "Content-Type": "application/json",
        "Authorization": main.apikeys[random.randint(0, len(main.apikeys) - 1)]
    }
    return headers


def chat_forget(msg: str) -> str:
    """
    切掉中间的对话，保留首尾，遗忘特性：保留谈话者认知，丢弃中途对话内容。
    """
    msg_list = msg.split()
    for i in range(2, 7):
        msg_list.pop(i)
    print("遗忘一次记忆")
    return "\n".join(msg_list)


chat_pool = list()


def get_chat(id: str):
    for i in chat_pool:

        if i["id"] == id:
            return i
    return False


def get_chat_history(id: str):
    return get_chat(id)["chat"]


def set_chat_history(id: str, target: str):
    for i in chat_pool:
        if i["id"] == id:
            i["chat"] = target


def prechat(id: str, feature: str):
    chat_single = dict()
    chat_single["id"] = id
    chat_single["chat"] = feature + "\n" + "你好。" + "\n"
    chat_pool.append(chat_single)


def chat(id: str, msg: str):
    chat_history = get_chat_history(id)
    if len(chat_history.split("\n")) > 10:
        chat_history = chat_forget(chat_history)
    chat_history += msg + "\n"
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": chat_history}],
    }
    response = r.post(url, json=data, headers=get_headers())
    answer = json.loads(response.text)["choices"][0]["message"]["content"]
    chat_history += answer + "\n"
    set_chat_history(id, chat_history)
    print(chat_history)
    return answer
