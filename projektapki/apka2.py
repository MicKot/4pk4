from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Dane(db.Model):
    __tablename__ = 'dane'
    id = db.Column('id',db.Integer, primary_key=True)
    created_at = db.Column('created_at',db.DateTime)
    patientnumber= db.Column('patientnumber',db.Integer)
    age = db.Column('age',db.Integer)
    sex = db.Column('sex',db.String)
    researchdate = db.Column('researchdate',db.String)
    roaddistance = db.Column('roaddistance',db.String)
    noise = db.Column('noise',db.Boolean)
    heating = db.Column('heating',db.String)
    education = db.Column('education',db.String)
    tobaccosmoke = db.Column('tobaccosmoke',db.String)
    smoking = db.Column('smoking',db.String)
    agesmoke = db.Column('agesmoke',db.Integer)
    regularsmoke = db.Column('regularsmoke',db.String)
    nocig = db.Column('nocig',db.String)
    anocigyeard = db.Column('anocigyeard',db.Integer)
    anocigyear1 = db.Column('anocigyear1',db.Integer)
    anocigyear2 = db.Column('anocigyear2',db.Integer)
    anocigyear5 = db.Column('anocigyear5',db.Integer)
    cigarbrand = db.Column('cigarbrand',db.String)
    quityear = db.Column('quityear',db.Integer)
    quit1year = db.Column('quit1year',db.Integer)
    quityear1 = db.Column('quityear1',db.Integer)
    quityear2 = db.Column('quityear2',db.Integer)
    quityear5 = db.Column('quityear5',db.Integer)
    quityear10 = db.Column('quityear10',db.Integer)
    quitcigarbrand = db.Column('quitcigarbrand',db.String)
    
db.create_all()

@app.route("/")
def welcome():
    return render_template('welcome2.html')


@app.route("/raw")
def show_form():
    fd = db.session.query(Dane).all()
    return render_template('raw.html', dane=fd)


@app.route('/results')
def show_kontakt():
    return render_template('results.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
