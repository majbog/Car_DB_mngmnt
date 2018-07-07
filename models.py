from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql.json import JSONB

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/cars_db'
db = SQLAlchemy(app)


class Brand(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    cars = db.relationship('Car', backref='car', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Car(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    model = db.Column(db.String(100))
    brand = db.Column(db.Integer, db.ForeignKey('brand.id'))
    info = db.Column(JSONB)

    def __init__(self, model, brand, info):
        self.model = model
        self.brand = brand
        self.info = info


if __name__ == '__main__':
    pass