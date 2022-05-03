from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import json

app = FastAPI()

class Sentence(BaseModel):
    id: int
    length: int
    width: int
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/greeting/")
def getGreeting(sentence: Sentence):
    s = json.loads(sentence.json())
    print(s)

    words = s["name"]
    words = words.split(" ")
    words.reverse()
    words  = " ".join(words)

    length = s["length"]
    length = length * 20

    width = s["width"]
    width = width * 20

    #s = s.upper()
    return {
        'status': "SUCCESS",
        "data" : words,
        "length": length,
        "width": 2,
        "area": width * length,
        "tokens": "a b c d e f g h i j k l m n o"
    }