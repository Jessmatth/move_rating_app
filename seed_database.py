"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

from crud import create_movie
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
    format = "%Y-%m-%d"
    movie["release_date"] = datetime.strptime(movie["release_date"], format) 
        #"2019-09-20"
    create_movie(movie["title"],movie["overview"], movie["release_date"], movie["poster_path"] ) 
    movies_in_db = movies_in_db.append()
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db