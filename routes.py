from flask import request, render_template, redirect, url_for
from datetime import datetime
from server import app, system

app = Flask(__name__)
currUser = None; #global variable that tracks the current user

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/add_blood', methods=['GET', 'POST'])
def add_blood():
    if request.method == 'GET':
        # Load page
        return render_template('add_blood.html', complete=False, errmsg='')
    elif request.method == 'POST':
        # Get information typed into page
        # Check for input value errors
        error = '';


        if error:
            # Input error occured, return error message
            return render_template('add_blood.html', complete=False, errmsg=error)
        else:
            # Input no error
            return render_template('add_blood.html', complete=True)