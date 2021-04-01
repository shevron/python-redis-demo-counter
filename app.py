"""FastAPI + Redis counter demo app
"""
import os

import redis
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

backend = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'),
                      port=int(os.environ.get('REDIS_PORT', '6379')))


@app.get('/{name}', response_class=PlainTextResponse)
def read(name: str):
    value = backend.get(name)
    if value is None:
        value = 0
    return str(int(value)) + "\n"


@app.post('/{name}', response_class=PlainTextResponse)
def read_item(name: str):
    value = backend.incr(name)
    return str(value) + "\n"
