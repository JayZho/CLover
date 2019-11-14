from flask import request, render_template, redirect, url_for, request
from datetime import datetime
from server import app, system

currUser = None; #global variable that tracks the current user

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
        bloodId = request.form["bloodId"] # int input
        bloodType = str(request.form.get("bloodType")) #drop down menu
        donor = int(request.form["donorId"]) #int id
        expire = request.form["expire"] #date input in string format
        origin = int(request.form["origin"]) #int id of medical facility

        arrival = datetime.now().date() #ARRIVAL DATE is date that it's added to the system
        expiry = datetime.strptime(expire, '%Y-%m-%d').date() # Convert string to datetime object

        # Input checking
        # Expiry date is before current date
        if expiry < arrival:
            error = "Invalid blood details - expiry date is before current date."

        if error:
            # Input error occured, return error message
            return render_template('add_blood.html', complete=False, errmsg=error)
        else:
            # Input no error
            bloodBag = system.addIncomingBlood(bloodId, bloodType, donor, expire, arrival, origin)
            print(bloodBag.toString())
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