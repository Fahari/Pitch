from flask_login import login_required
from flask import render_template
from . import main
# from app import app

@main.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
