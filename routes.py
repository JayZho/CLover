from flask import Flask, redirect, render_template, request, url_for, session, abort
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
