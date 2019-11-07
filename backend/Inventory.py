import datetime
from datetime import date
from BloodBag import BloodBag
from BloodType import BloodType

class Inventory:

    def __init__(self):
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

    # Creates and adds blood bag to respective blood type
    def addIncomingBloodBag(self, bloodType, donor, expire, arrival, origin):
        # Find bloodType to add to
        for bType in self._bloodTypes:
            # Equals correct blood type, add blood
            if bloodType == bType.getBloodTypes():
                bType.addIncomingBloodBag(donor, expire, arrival, origin)
                break


