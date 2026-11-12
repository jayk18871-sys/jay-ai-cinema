import uuid
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="JAY AI CINEMA X PRO MAX",
    version="5.0",
    description="AI Movie Generation Backend"
)

jobs = {}

class MovieRequest(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    duration: Literal[10, 60] = 10
    style: Literal[
        "Realistic Stick",
        "Cinematic 3D Cartoon",
        "Animal Cartoon",
        "Realistic 3D"
    ] = "Cinematic 3D Cartoon"
    language: Literal["Hindi", "English"] = "Hindi"
    quality: Literal["HD", "4K", "8K"] = "HD"
    description: str = ""

def create_scenes(duration, title, style, language):
    scenes = []
    count = duration

    for i in range(1, count + 1):
        scenes.append({
            "scene": i,
            "duration_minutes": 1,
            "title": f"{title} - Scene {i}",
            "visual_style": style,
            "language": language,
            "story_prompt": (
                f"Create a cinematic scene for {title}. "
                f"Maintain character consistency. "
                f"Scene number {i}. Style: {style}."
            )
        })

    return scenes

@app.get("/")
def home():
    return {
        "app": "JAY AI CINEMA X PRO MAX",
        "status": "online",
        "version": "5.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/generate")
def generate_movie(request: MovieRequest):

    movie_id = str(uuid.uuid4())

    batches = 1 if request.duration == 10 else 3

    scenes = create_scenes(
        request.duration,
        request.title,
        request.style,
        request.language
    )

    job = {
        "movie_id": movie_id,
        "title": request.title,
        "duration_minutes": request.duration,
        "style": request.style,
        "language": request.language,
        "quality": request.quality,
        "batches": batches,
        "batch_duration_minutes": 10 if batches == 1 else 20,
        "total_scenes": len(scenes),
        "scenes": scenes,
        "description": request.description,
        "status": "PLAN_CREATED",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "video_url": None
    }

    jobs[movie_id] = job

    return {
        "success": True,
        "message": "Movie production plan created",
        "movie": job,
        "next_step": "Connect a real AI video generation API"
    }

@app.get("/jobs/{movie_id}")
def get_job(movie_id: str):

    if movie_id not in jobs:
        raise HTTPException(
            status_code=404,
            detail="Movie job not found"
        )

    return jobs[movie_id]

@app.get("/movies")
def list_movies():
    return {
        "total": len(jobs),
        "movies": list(jobs.values())
    }
