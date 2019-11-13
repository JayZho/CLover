from flask import Flask
from BloodStorageSystem import BloodStorageSystem
from BloodType import BloodType
from BloodBag import BloodBag
from MedicalFacility import MedicalFacility
from datetime import datetime

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
