from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'vampire':
            return redirect(url_for('vampire'))
        elif request.form['username'] == 'medical':
            return redirect(url_for('medical'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/vampire_employee')
def vampire():
    return render_template('vampire_employee.html')

@app.route('/medical_facility')
def medical():
    return render_template('medical_facility.html')