import uuid
from datetime import datetime, timezone


class VideoGenerator:

    def __init__(self):
        self.name = "JAY AI CINEMA X PRO MAX"
        self.version = "5.0"

        self.supported_styles = [
            "Realistic Stick",
            "Cinematic 3D Cartoon",
            "Animal Cartoon",
            "Realistic 3D"
        ]

        self.supported_qualities = [
            "HD",
            "4K",
            "8K"
        ]

    def generate_video_plan(
        self,
        title,
        duration=10,
        style="Cinematic 3D Cartoon",
        quality="HD",
        language="Hindi",
        description=""
    ):

        if not title.strip():
            raise ValueError("Movie title is required")

        if duration not in [10, 60]:
            raise ValueError("Choose 10 or 60 minutes")

        if style not in self.supported_styles:
            raise ValueError("Invalid video style")

        if quality not in self.supported_qualities:
            raise ValueError("Invalid video quality")

        video_id = str(uuid.uuid4())

        scenes = []

        for i in range(1, duration + 1):

            scenes.append({
                "scene_id": i,
                "duration_minutes": 1,
                "title": f"{title} Scene {i}",
                "style": style,
                "quality": quality,
                "language": language,
                "prompt": (
                    f"Create cinematic scene {i} "
                    f"for {title}. "
                    f"Style: {style}. "
                    f"Quality target: {quality}. "
                    f"Language: {language}. "
                    f"Story: {description}. "
                    "Maintain character consistency, "
                    "smooth animation and cinematic lighting."
                )
            })

        return {
            "video_id": video_id,
            "title": title,
            "duration": duration,
            "style": style,
            "quality": quality,
            "language": language,
            "total_scenes": len(scenes),
            "scenes": scenes,
            "status": "PLAN_CREATED",
            "video_url": None,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }


video_generator = VideoGenerator()
