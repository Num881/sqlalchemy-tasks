from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_all_movies(session):
    movies = session.query(Movie).all()
    result = []
    for movie in movies:
        movie_str = (
            f"{movie.title} by {movie.director}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        result.append(movie_str)
    return result


def get_movies_by_director(session, director_name):
    movies = (
        session.query(Movie)
        .filter(Movie.director == director_name)
        .order_by(Movie.release_date)
        .all()
    )
    result = []
    for movie in movies:
        movie_str = (
            f"{movie.title} by {movie.director}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        result.append(movie_str)
    return result


def get_top_rated_movies(session, n):
    movies = (
        session.query(Movie)
        .order_by(Movie.rating.desc())
        .limit(n)
        .all()
    )
    result = []
    for movie in movies:
        movie_str = (
            f"{movie.title} by {movie.director}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        result.append(movie_str)
    return result
# END
