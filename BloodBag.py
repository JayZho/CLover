import datetime
from datetime import date

class BloodBag:


    def __init__(self, id, bloodType, donorId, expire, arrival, origin):
        self._id = id #int id
        self._bloodType = bloodType #string blood type
        self._donorId = donorId # int donorId
        self._expiryDate = expire # datetime date object
        self._arrivalDate = arrival # datetime date object
        self._origin = origin #int id of medical facility
    
    def getType(self):
        return self._bloodType
    
    def getDonor(self):
        return self._donor

    def getArrivalDate(self):
        return self._arrivalDate

    def getOrigin(self):
        return self._origin

    #check if the blood is expired
    def isExpired(self):
        return (self._expiryDate <= date.today())

    def getExpiryDate(self):
        return self._expiryDate

    def toString(self):
        return "ID: " + str(self._id) + ", Blood Type: " + self._bloodType + \
            ", Donor ID: " + str(self._donorId) + ", Expiry Date: " + str(self._expiryDate) + \
            ", Arrival Date: " + str(self._arrivalDate) + ", Origin: " + str(self._origin)