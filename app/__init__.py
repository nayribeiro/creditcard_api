from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creditcard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    # config_ma(app)

    Migrate(app, app.db)

    from .cards import bp_cards
    app.register_blueprint(bp_cards)

    return app
