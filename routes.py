from flask import Flask, redirect, render_template, request, url_for, session, abort
  #contains info about mfs for now, but will add more data to it later
from BloodStorageSystem import BloodStorageSystem

mfs = [1,2,3,4,5]
inventory = []

app = Flask(__name__)
system = BloodStorageSystem(inventory)

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

        # Get items out of form TODO Properly extract information
        # id, bloodType, donor, expire, arrival, origin
        bloodId = request.form["bloodId"]
        bloodType = request.form["bloodType"]
        donor = int(request.form["donorId"])
        expire = request.form["expire"]
        origin = request.form["origin"]

        arrival = datetime.now() #ARRIVAL DATE is date that it's added to the system

        # Input checking

        if error:
            # Input error occured, return error message
            return render_template('add_blood.html', complete=False, errmsg=error)
        else:
            # Input no error
            system.addIncomingBlood(bloodId, bloodType, donor, expire, arrival, origin)
            return render_template('add_blood.html', complete=True)

@app.route('/med-inventory')
def med_facility():
    list_a = [1, 2, 3]
    return render_template("inventory.html", listA = list_a, numberA = 20)

@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        type = request.form["bloodType"]
        amount = int(request.form["amount"])
        mfId = request.form["mf"]
        notes = request.form["notes"]

        for mf in system.getMFs():
            if mf.get_MF_id() == int(mfId):
                 medicalF = mf
                 break

        result = medicalF.sendRequest(type, amount, mfId, notes)

        print(result)
        if result == "error":
            return render_template("failure.html")

        return render_template('success.html')

    return render_template("make_request.html")
