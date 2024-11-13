from flask import render_template, url_for, request
from flaskapp.models import User

def register_routes(app, db):

    @app.route('/')
    def home():

        users = User.query.all()
        return render_template('home.html', title='Blue', users=users)
