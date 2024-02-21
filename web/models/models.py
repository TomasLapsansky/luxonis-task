from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(256), nullable=False)
