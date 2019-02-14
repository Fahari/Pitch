from flask_login import login_required
from flask import render_template
from app import app

@app.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('base.html')
