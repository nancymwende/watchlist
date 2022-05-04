from email import message
from flask import render_template
from app import app
#views

@app.route('/')
def index ():
    
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',title = title)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)