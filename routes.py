from flask import Flask, redirect, render_template, request, url_for, session, abort
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/med-inventory')
def med_facility():
    list_a = [1, 2, 3]
    return render_template("inventory.html", listA = list_a, numberA = 20)




