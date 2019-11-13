from flask import Flask, redirect, render_template, request, url_for, session, abort
import json

app = Flask(__name__)

self._user = "med"
system = Blo

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/med-inventory')
def med_facility():
    list_a = system.getListBloodType("A", , )
    list_b = system.getListBloodType("B", , )
    list_o = system.getListBloodType("O", , )
    list_ab = system.getListBloodType("AB", , )
    numberA = system.getQuantity("A")
    numberB = system.getQuantity("B")
    numberO = system.getQuantity("O")
    numberAB = system.getQuantity("AB")
    if(self._user == "med"):
        return render_template("inventory.html", numberA=numberA, numberB=numberB, numberO=numberO, numberAB=numberAB)
    elif(self._user == "vampire"):
        return render_template("inventory.html", listA = list_a, numberA = 20)





