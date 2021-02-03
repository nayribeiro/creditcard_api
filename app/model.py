from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Card(db.Model):
    exp_date = db.Column(db.String())
    holder = db.Column(db.String())
    number = db.Column(db.Integer, primary_key=True)
    cvv = db.Column(db.Integer())
