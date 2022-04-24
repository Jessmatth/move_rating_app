"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def returns_all_users():
    """Return information on all users"""

    return User.query.all()

def get_user_by_email(email):
    """Return user"""

    return User.query.filter(User.email == email).first()
    


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title,
                    overview=overview,
                    release_date=release_date,
                    poster_path=poster_path)

    return movie

def returns_all_movies():
    """Return all information on all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Get movie info by movie id."""

    return Movie.query.get(movie_id)
     

def create_rating(user, movie, score):
    """Create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)