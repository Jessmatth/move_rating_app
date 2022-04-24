"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

from crud import create_movie, create_user, create_rating
import model
import server

os.system("dropdb ratings")
# More code will go here
os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []

for movie in movie_data:
    date_format = "%Y-%m-%d"
    movie["release_date"] = datetime.strptime(movie["release_date"], date_format) 
        #"2019-09-20"
    movie_info=create_movie(movie["title"],movie["overview"], movie["release_date"], movie["poster_path"] ) 
    movies_in_db.append(movie_info)
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db

model.db.session.add_all(movies_in_db)
model.db.session.commit()

users_in_db = []
ratings_in_db = []

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    new_user = create_user(email, password)
    users_in_db.append(new_user)

    for i in range(10): 
        random_num = randint(1,5)
        random_movie = choice(movies_in_db)
        new_rating = create_rating(new_user, random_movie, random_num)
        ratings_in_db.append(new_rating)
        
        
model.db.session.add_all(users_in_db)  
model.db.session.add_all(ratings_in_db)  
model.db.session.commit() 
    
    