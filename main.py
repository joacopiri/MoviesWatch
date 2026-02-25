from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/ok")
def read_root():
    return {"status": "bien"}


@app.get("/movies-test")
def obtener_peliculas():
    r = requests.get("http://www.omdbapi.com/?apikey=f0ef6fdc&t=titanic")
    print(r)
    return r.json()

@app.get("/movies")
def movies():
    return {
        "peliculas": [
            "El Padrino",
            "La lista de Schindler",
            "Forrest Gump",
            "El caballero oscuro",
            "Inception",
            "Pulp Fiction",
            "El resplandor",
            "La guerra de las galaxias: Episodio IV - Una nueva esperanza",
            "Matrix",
            "El silencio de los corderos",
            "Titanic",
            "Gladiador",
            "Avengers: Endgame",
            "El lobo de Wall Street",
            "La naranja mecánica",
            "Interstellar",
            "El secreto de sus ojos",
            "Jurassic Park",
            "Cazafantasmas",
            "Parásitos",
            "Volver",
            "The Shawshank Redemption",
            "La vida es bella",
            "Seven",
            "The Dark Knight Rises",
            "La princesa Mononoke",
            "Trainspotting",
            "El club de la pelea",
            "El buen, el malo y el feo",
            "2001: Una odisea del espacio",
            "Los Increíbles",
            "V de Vendetta",
            "Mad Max: Fury Road",
            "Scarface",
            "Pulp Fiction",
            "La forma del agua",
            "Whiplash",
            "Unforgiven",
            "Psicosis",
            "Amélie",
            "Memento",
            "El Gran Lebowski",
            "Gladiador",
            "Los siete samuráis",
            "City of God",
            "Scream",
            "El viaje de Chihiro",
            "Los cazadores del arca perdida",
            "No Country for Old Men",
            "Requiem for a Dream",
            "Her"
        ]
    }