class MovieEngine:

    def __init__(self):
        self.name = "JAY AI CINEMA X"

    def create_movie_plan(
        self,
        title,
        style,
        duration=60,
        language="Hindi"
    ):
        return {
            "engine": self.name,
            "movie_title": title,
            "visual_style": style,
            "duration_minutes": duration,
            "language": language,
            "status": "Plan Created"
        }
