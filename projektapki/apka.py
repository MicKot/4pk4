from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)


class Formdata(db.Model):
    __tablename__ = 'dane'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    patientnumber= db.Column(db.Integer)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    researchdate = db.Column(db.String)
    roaddistance = db.Column(db.String)
    noise = db.Column(db.Boolean)
    heating = db.Column(db.String)
    education = db.Column(db.String)
    tobaccosmoke = db.Column(db.String)
    smoking = db.Column(db.String)
    agesmoke = db.Column(db.Integer)
    regularsmoke = db.Column(db.String)
    nocig = db.Column(db.String)
    anocigyeard = db.Column(db.Integer)
    anocigyear1 = db.Column(db.Integer)
    anocigyear2 = db.Column(db.Integer)
    anocigyear5 = db.Column(db.Integer)
    cigarbrand = db.Column(db.String)
    quityear = db.Column(db.Integer)
    quit1year = db.Column(db.Integer)
    quityear1 = db.Column(db.Integer)
    quityear2 = db.Column(db.Integer)
    quityear5 = db.Column(db.Integer)
    quityear10 = db.Column(db.Integer)
    quitcigarbrand = db.Column(db.String)


    def __init__(self, patientnumber,age, sex, researchdate, birthplace, yearsliving, roaddistance, noise, heating, education, tobaccosmoke,
                 smoking, agesmoke,
                 regularsmoke, nocig, anocigyear, anocigyear1, anocigyear2, anocigyear5, cigarbrand, quityear,
                 quit1year, quityear1, quityear2, quityear5,
                 quityear10, quitcigarbrand):
        self.patientnumber = patientnumber
        self.age = age
        self.sex = sex
        self.researchdate = researchdate
        self.birthplace = birthplace
        self.yearsliving = yearsliving
        self.roaddistance = roaddistance
        self.noise = noise
        self.heating = heating
        self.education = education
        self.tobaccosmoke = tobaccosmoke
        self.smoking = smoking
        self.agesmoke = agesmoke
        self.regularsmoke = regularsmoke
        self.nocig = nocig
        self.anocigyeard = anocigyear
        self.anocigyear1 = anocigyear1
        self.anocigyear2 = anocigyear2
        self.anocigyear5 = anocigyear5
        self.cigarbrand = cigarbrand
        self.quityear = quityear
        self.quit1year = quit1year
        self.quityear1 = quityear1
        self.quityear2 = quityear2
        self.quityear5 = quityear5
        self.quityear10 = quityear10
        self.quitcigarbrand = quitcigarbrand



db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')


@app.route("/form")
def show_form():
    return render_template('form.html')


@app.route('/kontakt')
def show_kontakt():
    return render_template('kontakt.html')


@app.route('/dziekuje.html')
def dziekuje():
    return render_template('dziekuje.html')


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    patientnumber=request.form['patientnumber']
    age = request.form['age']
    sex = request.form['sex']
    researchdate = request.form['researchdate']
    birthplace = request.form['birthplace']
    yearsliving = request.form['yearsliving']
    roaddistance = request.form['roaddistance']
    noise = request.form['noise']
    heating = request.form['heating']
    education = request.form['education']
    tobaccosmoke = request.form['tobaccosmoke']
    smoking = request.form['smoking']
    agesmoke = request.form['agesmoke']
    regularsmoke = request.form['regularsmoke']
    nocig = request.form['nocig']
    anocigyear = request.form['anocigyear']
    anocigyear1 = request.form['anocigyear1']
    anocigyear2 = request.form['anocigyear2']
    anocigyear5 = request.form['anocigyear5']
    cigarbrand = request.form['cigarbrand']
    quityear = request.form['quityear']
    quit1year = request.form['quit1year']
    quityear1 = request.form['quityear1']
    quityear2 = request.form['quityear2']
    quityear5 = request.form['quityear5']
    quityear10 = request.form['quityear10']
    quitcigarbrand = request.form['quitcigarbrand']



    # Save the data
    fd = Formdata(patientnumber, age, sex, researchdate, birthplace, yearsliving, roaddistance, noise, heating, education, tobaccosmoke, smoking,
                  agesmoke, regularsmoke, nocig,
                  anocigyear, anocigyear1, anocigyear2, anocigyear5, cigarbrand, quityear, quit1year, quityear1,
                  quityear2, quityear5, quityear10, quitcigarbrand)

    db.session.add(fd)
    db.session.commit()

    return redirect('/dziekuje.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
