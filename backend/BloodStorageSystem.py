import datetime
from datetime import date
from Inventory import Inventory

class BloodStorageSystem:


    def __init__(self, inventory):
        self._medFacilities = []
        self._inventory = inventory
       
    
    def addBloodType(self, bloodType):
        self._bloodTypes.append(bloodType)

    def getBloodTypes(self):
        return self._bloodTypes

    def giveWarning(self):
        pass
    
    # Add incoming blood bag to inventory
    def addIncomingBlood(self, bloodType, donor, expire, arrival, origin):
        # TODO Parse input to check for correctness

        # Adds blood to system
        self._inventory.addIncomingBloodBag(bloodType, donor, expire, arrival, origin)
