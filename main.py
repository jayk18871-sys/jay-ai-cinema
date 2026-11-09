from fastapi import FastAPI
from pydantic import BaseModel
from movie_engine import MovieEngine

app = FastAPI(title="JAY AI CINEMA X")

engine = MovieEngine()

class MovieRequest(BaseModel):
    title: str
    style: str = "Realistic 3D"
    duration: int = 30
    language: str = "Hindi"

@app.get("/")
def home():
    return {
        "name": "JAY AI CINEMA X",
        "status": "Online"
    }

@app.post("/create-movie")
def create_movie(movie: MovieRequest):
    return engine.create_movie_plan(
        movie.title,
        movie.style,
        movie.duration,
        movie.language
    )
