from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('welcome.html')


@app.route("/form")
def show_form():
    return render_template('form2.html')


@app.route('/kontakt')
def show_kontakt():
    return render_template('kontakt.html')

@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    firstname = request.form['firstname']
    email = request.form['email']
    age = request.form['age']
    income = request.form['income']
    satisfaction = request.form['satisfaction']
    q1 = request.form['q1']
    q2 = request.form['q2']

    # Save the data
    fd = Formdata(firstname, email, age, income, satisfaction, q1, q2)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
