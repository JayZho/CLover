import datetime
from datetime import date

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
    
    