from flask import render_template, request, redirect, url_for
from . import main
from ..models import Review

@main.route('/')
def index():
    message = 'Its awesome'
    title = 'Home - Simply the best movies'

    return render_template('index.html', message = message, title = title)