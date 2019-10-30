import datetime
from datetime import date

class Inventory:

    def __init__(self, type):
        self._bloodTypes = []
       
    
    def addBloodType(self, bloodType):
        self._bloodTypes.append(bloodType)

    def getBloodTypes(self):
        return self._bloodTypes

    def clearExpriedBlood(self):
        for bloodType in self._bloodTypes:
            bloodType.removeExpiredBlood()

    def checkCritical(self):
        for bloodType in self._bloodTypes:
            pass



    
