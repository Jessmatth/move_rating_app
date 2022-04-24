"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from flask import Flask

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Route to homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """Display all movies on the movies route."""

    movies = crud.returns_all_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show movie information"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/movies/<movie_id>', methods=['POST'])
def rate_movie(rating):
    """""Save movie rating"""
    rating = request.form.get("rating")

    new_rating = crud.create_rating(session['user'],'<movie_id>', rating)
    db.session.add(new_rating)  
    db.session.commit() 

    return redirect('/movies')

@app.route('/users/')
def show_user():
    """Show user information"""

    users = crud.returns_all_users()

    return render_template('all_users.html', users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Create and check user"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash('You cannot create an account with this email, try again.')
    else:
        new_user = crud.create_user(email,password)
        db.session.add(new_user)  
        db.session.commit() 
        flash('Your account has been created successfully.')

    return redirect("/")

@app.route("/login", methods =["POST"])
def login_user():
    """Login the user"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        if password == user.password:
            session['user_id'] = user.user_id
            flash('Logged in')

    else:
        flash('Your password does not match')
    
    return redirect('/')




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
