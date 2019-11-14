from flask import Flask
from BloodStorageSystem import BloodStorageSystem
from BloodType import BloodType
from BloodBag import BloodBag
from MedicalFacility import MedicalFacility
from datetime import datetime
import csv

# Flask application
app = Flask(__name__)

# Initialise system
system = BloodStorageSystem()

# Load in medical facilities
med1 = MedicalFacility("Medical Facility", 1, system)
system.addMedFacility(med1)
med2 = MedicalFacility("Medical Facility Facility", 2, system)
system.addMedFacility(med2)

# Load in blood types and limit amounts
typeA = BloodType("A", 5)
typeB = BloodType("B", 5)
typeAB = BloodType("AB", 5)
typeO = BloodType("O", 5)
system.addBloodType(typeA)
system.addBloodType(typeB)
system.addBloodType(typeAB)
system.addBloodType(typeO)

# Load in blood bags
# blood.csv contains data for blood bags
# each row is a new blood bag with:
# ID, BloodType, Donor ID, Expiry Date, Medical Facility ID
with open('data/blood.csv', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, dialect='excel', delimiter=',')

    for row in csv_reader:
        # Check values
        print(row)

        # Get data
        # NOTE encoded with UT8, has BOM at front
        # Decode with utf-8-sig to remove BOM
        # i.e. utf-8  w/ BOM decoded with utf-8  u'\ufeffABC'
        # https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
        bloodId = int(row[0]) 
        bloodType = str(row[1])
        donorId = int(row[2])
        expiryDate = datetime.strptime(str(row[3]), '%Y-%m-%d').date()
        arrival = datetime.now().date()
        medFac = int(row[4])
        
        # Make blood
        bag = BloodBag(bloodId, bloodType, donorId, expiryDate, arrival, medFac)
        print(bag.toString())

        # Insert under correct blood type
        if bloodType == "A":
            system._bloodTypes[0].addBloodBag(bag)
            #print(system._bloodTypes[0].getBloodType())
        elif bloodType == "B":
            system._bloodTypes[1].addBloodBag(bag)
            #print(system._bloodTypes[1].getBloodType())
        elif bloodType == "AB":
            system._bloodTypes[2].addBloodBag(bag)
            #print(system._bloodTypes[2].getBloodType())
        elif bloodType == "O":
            system._bloodTypes[3].addBloodBag(bag)
            #print(system._bloodTypes[3].getBloodType())
        