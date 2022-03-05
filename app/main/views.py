from flask import render_template, request, redirect, url_for

from app.requests import get_movies
from . import main
from ..models import Review

@main.route('/')
def index():
    message = 'Its awesome'
    title = 'Home - Simply the best movies'
    popular_movies = get_movies('popular')

    return render_template('index.html', message = message, title = title, popular = popular_movies)