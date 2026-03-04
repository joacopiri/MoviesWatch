from fastapi import FastAPI
import requests
import os
from data import peliculas

app = FastAPI()


@app.get("/ok")
def read_root():
    if not "APIKEY_OMDBAPI" in os.environ.keys():
        return {"status": "nokey"}
    return {"status": "ok"}


@app.get("/movies-test")
def obtener_peliculas():
    r = requests.get(f"http://www.omdbapi.com/?apikey={os.environ.get("APIKEY_OMDBAPI")}&t=titanic")
    return r.json()

@app.get("/movies")
def movies():
    return peliculas

@app.get("/movies/{pelicula}")
def movies_by_id(pelicula:str):
    r_id = requests.get(f"http://www.omdbapi.com/?apikey={os.environ.get("APIKEY_OMDBAPI")}&t={pelicula}")
    return r_id.json()