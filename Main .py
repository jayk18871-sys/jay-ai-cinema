from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="JAY AI CINEMA X",
    version="1.0.0"
)

class MovieRequest(BaseModel):
    title: str
    style: str = "realistic"
    duration_minutes: int = 60
    language: str = "Hindi"

@app.get("/")
def home():
    return {
        "engine": "JAY AI CINEMA X",
        "status": "Ready"
    }

@app.post("/create-movie")
def create_movie(movie: MovieRequest):
    return {
        "title": movie.title,
        "style": movie.style,
        "duration": movie.duration_minutes,
        "language": movie.language,
        "status": "Planning"
    }
