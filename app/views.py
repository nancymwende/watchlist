from email import message
from flask import render_template
from app import app
from request import get_movies
#views

@app.route('/')
def index ():
    
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming_movie')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',title = title,popular = popular_movies,upcoming = upcoming_movie,now_showing = now_showing_movie )

@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)
    
    

