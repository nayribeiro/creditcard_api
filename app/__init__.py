from flask import Flask
from flask_migrate import Migrate, migrate
from .model import configure as config_db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creditcard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.model import Card

    config_db(app)
    # migrate =  Migrate(app, app.db)
    migrate = Migrate()

    migrate.init_app(app, app.db)

    from .cards import bp_cards
    app.register_blueprint(bp_cards)

    return app
