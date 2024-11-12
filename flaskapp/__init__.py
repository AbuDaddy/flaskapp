from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    from flaskapp.routes import register_routes
    register_routes(app, db)

    migrate.init_app(app, db)
    return app
