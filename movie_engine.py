import uuid
from datetime import datetime, timezone


class MovieEngine:

    def __init__(self):
        self.name = "JAY AI CINEMA X PRO MAX"
        self.version = "5.0"

        self.styles = [
            "Realistic Stick",
            "Cinematic 3D Cartoon",
            "Animal Cartoon",
            "Realistic 3D"
        ]

        self.qualities = ["HD", "4K", "8K"]

    def generate_movie(
        self,
        title,
        duration=10,
        style="Cinematic 3D Cartoon",
        language="Hindi",
        quality="HD",
        description=""
    ):

        if not title.strip():
            raise ValueError("Movie title is required")

        if duration not in [10, 60]:
            raise ValueError("Duration must be 10 or 60 minutes")

        if style not in self.styles:
            raise ValueError("Invalid movie style")

        if quality not in self.qualities:
            raise ValueError("Invalid video quality")

        movie_id = str(uuid.uuid4())

        total_scenes = duration
        total_batches = 1 if duration == 10 else 3

        scenes = []

        for i in range(1, total_scenes + 1):

            scenes.append({
                "scene_number": i,
                "duration_minutes": 1,
                "scene_title": f"{title} Scene {i}",
                "visual_style": style,
                "language": language,
                "quality": quality,
                "prompt": (
                    f"Create scene {i} for movie {title}. "
                    f"Visual style: {style}. "
                    f"Language: {language}. "
                    f"Story: {description}. "
                    "Maintain consistent characters, "
                    "cinematic lighting and smooth animation."
                )
            })

        return {
            "movie_id": movie_id,
            "title": title,
            "duration_minutes": duration,
            "style": style,
            "language": language,
            "quality": quality,
            "total_batches": total_batches,
            "total_scenes": total_scenes,
            "scenes": scenes,
            "status": "PLAN_CREATED",
            "video_generated": False,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }


movie_engine = MovieEngine()
