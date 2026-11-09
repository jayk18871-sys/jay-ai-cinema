from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="JAY AI CINEMA X")

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
    return {
        "message": "Movie request received",
        "title": movie.title,
        "style": movie.style,
        "duration": movie.duration,
        "language": movie.language
    }
