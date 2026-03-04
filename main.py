from fastapi import FastAPI
import requests
import os
from data import peliculas

app = FastAPI()


@app.get("/ok")
def read_root():
    return {"status": "ok"}


@app.get("/movies-test")
def obtener_peliculas():
    r = requests.get(f"http://www.omdbapi.com/?apikey={os.environ.get("APIKEY_OMDBAPI")}&t=titanic")
    print(r)
    return r.json()

@app.get("/movies")
def movies():
    return peliculas