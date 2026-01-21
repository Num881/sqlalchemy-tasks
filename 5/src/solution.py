from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    result = []

    # Используем join для объединения таблиц movies и directors
    movies_with_directors = (
        session.query(Movie, Director.name)
        .join(Director, Movie.director_id == Director.id)
        .order_by(Movie.title)
        .all()
    )

    for movie, director_name in movies_with_directors:
        movie_str = (
            f"{movie.title} by {director_name}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        result.append(movie_str)

    return result
# END
