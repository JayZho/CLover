
from flask import request, render_template, redirect, url_for, request
from datetime import datetime
from server import app, system


currUser = None; #global variable that tracks the current user



@app.route('/')
@app.route('/index')
def index():
    return "Hello"


@app.route('/vampire_employee')
def vampire(start, end):
    #converting strings to datetime objects
    startDate = datetime.strptime(start, "%d/%m/%Y")
    endDate = datetime.strptime(end, "%d/%m/%Y")

    list_a = system.getListBloodType("A", startDate, endDate)
    list_b = system.getListBloodType("B", startDate, endDate)
    list_o = system.getListBloodType("O", startDate, endDate)
    list_ab = system.getListBloodType("AB", startDate, endDate)
    numberA = system.getQuantity("A")
    numberB = system.getQuantity("B")
    numberO = system.getQuantity("O")
    numberAB = system.getQuantity("AB")
    return render_template('vampire_employee.html', numberA=numberA, numberB=numberB, numberO=numberO, numberAB=numberAB,
                            listA = list_a, listB = list_b, listAB = list_ab, listO = list_o)


@app.route('/medical_facility')
def medical():
    numberA = system.getQuantity("A")
    numberB = system.getQuantity("B")
    numberO = system.getQuantity("O")
    numberAB = system.getQuantity("AB")
    return render_template('medical_facility.html', numberA=numberA, numberB=numberB, numberO=numberO, numberAB=numberAB)


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
