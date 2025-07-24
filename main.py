# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "from deployed app!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)