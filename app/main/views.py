from flask import render_template, request, redirect, url_for

from app.requests import get_movies, search_movie
from . import main
from ..models import Review

@main.route('/')
def index():
    message = 'Its awesome'
    title = 'Home - Simply the best movies'
    popular_movies = get_movies('popular')

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', message = message, title = title, popular = popular_movies)

@main.route('/search/<movie_name>')
def search(movie_name):

    movie_name_list = movie_name.split('')
    movie_name_format = '+'.join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies = searched_movies)