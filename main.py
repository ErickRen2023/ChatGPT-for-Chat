from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
async def main():
    return JSONResponse({
        "code": 200,
        "data": {"result": "OK"}
    })
