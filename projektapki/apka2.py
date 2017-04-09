from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dane.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

@app.route("/")
def welcome():
    return render_template('welcome2.html')


@app.route("/raw")
def show_form():
    return render_template('raw.html')


@app.route('/results')
def show_kontakt():
    return render_template('results.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
